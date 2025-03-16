from flask import Blueprint, jsonify

from ..extensions import db
from ..models.periodo import Periodo


periodo = Blueprint('periodo', __name__)

@periodo.route("/periodo")
def periodo_json():
    resp = db.session.execute(db.select(Periodo)).scalars().all()

    return jsonify(resp)