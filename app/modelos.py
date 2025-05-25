from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    numero_de_identificacao = db.Column(db.Integer, nullable=False)


class Evento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=True)


class Presenca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    evento_id = db.Column(db.Integer, db.ForeignKey('evento.id'), nullable=False)
    
    # Mapeia a relação com as tabelas Usuario e Evento
    usuario = db.relationship('Usuario', backref=db.backref('presencas', lazy=True))
    evento = db.relationship('Evento', backref=db.backref('presencas', lazy=True))
