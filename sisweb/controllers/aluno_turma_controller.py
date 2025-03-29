# from flask import Blueprint, jsonify

from extensions import db
from models.aluno_turma import AlunoTurma


# aluno_turma = Blueprint('aluno_turma', __name__)

# @aluno_turma.route("/aluno-turma")
# def aluno_turma_json():
#     alunos = db.session.execute(db.select(AlunoTurma)).scalars().all()

#     return jsonify(alunos)