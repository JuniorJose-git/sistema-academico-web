from flask import Blueprint, jsonify

from ..extensions import db
from ..models.sala_de_aula import SalaDeAula


sala_de_aula = Blueprint('sala_de_aula', __name__)


@sala_de_aula.route("/sala-de-aula")
def sala_de_aula_json():
    resp = db.session.execute(db.select(SalaDeAula)).scalars().all()

    return jsonify(resp)