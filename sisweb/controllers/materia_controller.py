from flask import Blueprint, jsonify

from ..extensions import db
from ..models.materia import Materia


materia = Blueprint('materia', __name__)


@materia.route("/materia")
def materia_json():
    resp = db.session.execute(db.select(Materia)).scalars().all()

    return jsonify(resp)