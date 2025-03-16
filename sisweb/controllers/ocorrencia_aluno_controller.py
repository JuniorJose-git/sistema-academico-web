from flask import Blueprint, jsonify

from ..extensions import db
from ..models.ocorrencia_aluno import OcorrenciaAluno


ocorrencia_aluno = Blueprint('ocorrencia_aluno', __name__)

@ocorrencia_aluno.route("/ocorrencia-aluno")
def ocorrencia_aluno_json():
    resp = db.session.execute(db.select(OcorrenciaAluno)).scalars().all()

    return jsonify(resp)