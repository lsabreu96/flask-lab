from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import validates, ValidationError, fields
from app.modelos import Usuario, Evento, Presenca

class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        # permite fazer mecanismos de serialização e desserialização
        load_instance = True

    @validates('numero_de_identificacao')
    #  Isso indica que o Marshmallow está chamando seu método de validação com um argumento a mais (como data_key), e seu validador não aceita.
    def validate_numero_de_identificacao(self, value, **kwargs):
        if value % 2 != 0:
            raise ValidationError('O número de identificação deve ser múltiplo de 2.')


class EventoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Evento
        load_instance = True

class PresencaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Presenca
        load_instance = True
