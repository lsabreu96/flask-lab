from flask import Blueprint, request, jsonify
from app.modelos import Usuario, db
from app.schemas import UsuarioSchema

bp_usuario = Blueprint('bp_usuario', __name__, url_prefix='/usuario')
usuario_schema = UsuarioSchema(session=db.session)
usuarios_schema = UsuarioSchema(many=True)

# GET /usuario
@bp_usuario.route('/', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    usuarios = usuarios_schema.dump(usuarios, many=True)
    return jsonify(usuarios), 200

# GET /usuario/<id>
@bp_usuario.route('/<int:id>', methods=['GET'])
def get_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    usuario = usuario_schema.dump(usuario)
    return jsonify(usuario), 200

# POST /usuario
@bp_usuario.route('/', methods=['POST'])
def create_usuario():
    data = request.json
    try:
        usuario = usuario_schema.load(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

    db.session.add(usuario)
    db.session.commit()
    
    return jsonify(usuario_schema.dump(usuario)), 201

# PUT /usuario/<id>
@bp_usuario.route('/<int:id>', methods=['PUT'])
def update_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    data = request.json
    try:
        updated_data = usuario_schema.load(data, partial=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
    db.session.commit()
    return usuario_schema.jsonify(usuario_schema.dump(updated_data)), 200
