# from flask import Blueprint, jsonify

from extensions import db
from models.horario import Horario


# horario = Blueprint('horario', __name__)


# @horario.route("/sala-de-aula")
# def horario_json():
#     resp = db.session.execute(db.select(Horario)).scalars().all()

#     return jsonify(resp)