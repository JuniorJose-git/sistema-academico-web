from flask import Blueprint, jsonify

from ..extensions import db
from ..models.dia_horario import DiaHorario


dia_horario = Blueprint('dia_horario', __name__)

@dia_horario.route("/dia-horario")
def dia_horario_json():
    resp = db.session.execute(db.select(DiaHorario)).scalars().all()

    return jsonify(resp)