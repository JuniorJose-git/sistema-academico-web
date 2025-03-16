from flask import Blueprint, jsonify

from ..extensions import db
from ..models.professor import Professor


professor = Blueprint('professor', __name__)


@professor.route("/professor")
def professor_json():
    resp = db.session.execute(db.select(Professor)).scalars().all()

    return jsonify(resp)