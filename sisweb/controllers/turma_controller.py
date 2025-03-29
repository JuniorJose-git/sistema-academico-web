# from flask import Blueprint, jsonify

from extensions import db
from models.turma import Turma


# turma = Blueprint('turma', __name__)

# @turma.route("/turma")
# def turma_json():
#     resp = db.session.execute(db.select(Turma)).scalars().all()

#     return jsonify(resp)