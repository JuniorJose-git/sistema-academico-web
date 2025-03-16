from flask import Blueprint, jsonify

from ..extensions import db
from ..models.turma_dia_horario import TurmaDiaHorario


turma_dia_horario = Blueprint('turma_dia_horario', __name__)

@turma_dia_horario.route("/turma-dia-horario")
def turma_dia_horario_json():
    resp = db.session.execute(db.select(TurmaDiaHorario)).scalars().all()

    return jsonify(resp)