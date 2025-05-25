from flask import Blueprint, request, jsonify
from app.modelos import db, Evento
from app.schemas import EventoSchema

bp_evento = Blueprint('evento', __name__, url_prefix='/evento')
evento_schema = EventoSchema(session=db.session)
eventos_schema = EventoSchema(many=True)


@bp_evento.route('/', methods=['GET'])
def listar_eventos():
    eventos = Evento.query.all()
    eventos = eventos_schema.dump(eventos, many=True)
    return jsonify(eventos)


@bp_evento.route('/<int:id>', methods=['GET'])
def encontra_eventos(id):
    evento = Evento.query.get_or_404(id)
    evento = evento_schema.dump(evento)
    return jsonify(evento)


@bp_evento.route('/', methods=['POST'])
def criar_evento():
    data = request.json
    try:
        evento = evento_schema.load(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

    db.session.add(evento)
    db.session.commit()
    return jsonify(evento_schema.dump(evento)), 201


@bp_evento.route('/<int:id>', methods=['PUT'])
def atualizar_evento(id):
    evento = Evento.query.get_or_404(id)
    data = request.json
    try:
        evento = evento_schema.load(data, instance=evento, partial=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    db.session.commit()
    return jsonify(evento_schema.dump(evento)), 200


@bp_evento.route('/<int:id>', methods=['DELETE'])
def deletar_evento(id):
    evento = Evento.query.get_or_404(id)
    db.session.delete(evento)
    db.session.commit()
    return '', 204
