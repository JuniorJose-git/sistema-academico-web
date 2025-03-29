# from flask import Blueprint, jsonify

from extensions import db
from models.responsavel import Responsavel


# responsavel = Blueprint('responsavel', __name__)


# @responsavel.route("/responsavel")
# def responsavel_json():
#     resp = db.session.execute(db.select(Responsavel)).scalars().all()

#     return jsonify(resp)