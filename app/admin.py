from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.modelos import db, Usuario, Presenca

admin = Admin(name='Admin', template_mode='bootstrap3')

# ModelView que permite apenas CRIAÇÃO
class ReadOnlyModelView(ModelView):
    can_create = True
    can_edit = False
    can_delete = False
    can_view_details = True
    column_display_pk = True

def configurar_admin(app):
    admin.init_app(app)

    admin.add_view(ReadOnlyModelView(Usuario, db.session))

    admin.add_view(ReadOnlyModelView(Presenca, db.session))
