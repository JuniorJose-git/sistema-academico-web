# from flask import Blueprint, jsonify

from extensions import db
from models.disciplina import Disciplina


# disciplina = Blueprint('disciplina', __name__)


# @disciplina.route("/disciplina")
# def disciplina_json():
#     resp = db.session.execute(db.select(Disciplina)).scalars().all()

#     return jsonify(resp)