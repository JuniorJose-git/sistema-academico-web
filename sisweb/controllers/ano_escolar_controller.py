from flask import Blueprint, jsonify

from ..extensions import db
from ..models.ano_escolar import AnoEscolar


ano_escolar = Blueprint('ano_escolar', __name__)

@ano_escolar.route("/ano-escolar")
def ano_escolar_json():
    resp = db.session.execute(db.select(AnoEscolar)).scalars().all()

    return jsonify(resp)