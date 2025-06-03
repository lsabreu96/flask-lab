from flask import Flask
from app.modelos import db
from app.rotas.usuario import bp_usuario
from app.rotas.evento import bp_evento
from app.rotas.presenca import bp_presenca
from app.admin import configurar_admin
import os 

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(bp_usuario)
    app.register_blueprint(bp_evento)
    app.register_blueprint(bp_presenca)

    configurar_admin(app)

    with app.app_context():
        db.create_all()

    return app
