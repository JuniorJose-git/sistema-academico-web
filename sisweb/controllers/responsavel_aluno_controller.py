from flask import Blueprint, jsonify

from ..extensions import db
from ..models.responsavel_aluno import ResponsavelAluno


responsavel_aluno = Blueprint('responsavel_aluno', __name__)

@responsavel_aluno.route("/responsavel-aluno")
def responsavel_aluno_json():
    resp = db.session.execute(db.select(ResponsavelAluno)).scalars().all()

    return jsonify(resp)