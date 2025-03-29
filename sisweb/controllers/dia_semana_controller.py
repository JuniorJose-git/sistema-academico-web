# from flask import Blueprint, jsonify

from extensions import db
from models.dia_semana import DiaSemana


# dia_semana = Blueprint('dia_semana', __name__)


# @dia_semana.route("/dia-semana")
# def dia_semana_json():
#     resp = db.session.execute(db.select(SalaDeAula)).scalars().all()

#     return jsonify(resp)