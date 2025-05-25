from flask import Blueprint, request, jsonify
from app.modelos import db, Presenca
from app.schemas import PresencaSchema

bp_presenca = Blueprint('presenca', __name__, url_prefix='/presenca')
presenca_schema = PresencaSchema(session=db.session)
presencas_schema = PresencaSchema(many=True)

@bp_presenca.route('/', methods=['GET'])
def listar_presencas():
    presencas = Presenca.query.all()
    return presencas_schema.jsonify(presencas)

@bp_presenca.route('/', methods=['POST'])
def criar_presenca():
    data = request.json
    try:
        presenca = presenca_schema.load(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    db.session.add(nova_presenca)
    db.session.commit()
    return presenca_schema.jsonify(nova_presenca), 201

@bp_presenca.route('/<int:id>', methods=['PUT'])
def atualizar_presenca(id):
    presenca = Presenca.query.get_or_404(id)
    data = request.json
    try:
        presenca = presenca_schema.load(data, instance=presenca, partial=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    db.session.commit()
    return presenca_schema.jsonify(presenca)
