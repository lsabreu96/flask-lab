from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.modelos import db, Usuario, Presenca

admin = Admin(name='Admin', template_mode='bootstrap3')

class CreateReadOnlyModelView(ModelView):
    can_create = True
    can_edit = False
    can_delete = False
    can_view_details = True
    column_display_pk = True


class PresencaModelView(CreateReadOnlyModelView):
    # tava dando algum erro maluco com a relação, então vamos mostrar só os IDs
    form_columns = ['usuario_id', 'evento_id'] 

class UsuarioModelView(CreateReadOnlyModelView):
    form_columns = ['nome', 'numero_de_identificacao']

    def __init__(self, model, session, **kwargs):
        super().__init__(model, session, **kwargs)
        from app.schemas import UsuarioSchema  # ajuste conforme sua estrutura
        self.schema = UsuarioSchema(session=db.session)  # <<< instanciando o schema

    def on_model_change(self, form, model, is_created):
        errors = self.schema.validate({
            "nome": model.nome,
            "numero_de_identificacao": model.numero_de_identificacao
        })
        if errors:
            raise ValueError(errors)


def configurar_admin(app):
    admin.init_app(app)

    admin.add_view(UsuarioModelView(Usuario, db.session))
    admin.add_view(PresencaModelView(Presenca, db.session))
