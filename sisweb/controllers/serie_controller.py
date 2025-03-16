from flask import Blueprint, jsonify

from ..extensions import db
from ..models.serie import Serie

serie = Blueprint('serie', __name__)


@serie.route("/serie")
def serie_json():
    resp = db.session.execute(db.select(Serie)).scalars().all()

    return jsonify(resp)