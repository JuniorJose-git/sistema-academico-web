from flask import Blueprint, jsonify

from ..extensions import db
from ..models.coordenador import Coordenador


coordenador = Blueprint('coordenador', __name__)


@coordenador.route("/coordenador")
def coordenador_json():
    resp = db.session.execute(db.select(Coordenador)).scalars().all()

    return jsonify(resp)