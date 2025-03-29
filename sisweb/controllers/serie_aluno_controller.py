# from flask import Blueprint, jsonify

from extensions import db
from models.serie_aluno import SerieAluno

# serie_aluno = Blueprint('serie_aluno', __name__)


# @serie_aluno.route("/serie-aluno")
# def serie_aluno_json():
#     resp = db.session.execute(db.select(SerieAluno)).scalars().all()

#     return jsonify(resp)