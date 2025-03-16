from flask import Blueprint, jsonify

from ..extensions import db
from ..models.aluno import Aluno


aluno = Blueprint('aluno', __name__)

@aluno.route("/aluno")
def aluno_json():
    resp = db.session.execute(db.select(Aluno)).scalars().all()

    return jsonify(resp)