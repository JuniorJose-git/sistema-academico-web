# from flask import Blueprint, jsonify

from extensions import db
from models.chamada import Chamada


# chamada = Blueprint('chamada', __name__)

# @chamada.route("/chamada")
# def chamada_json():
#     resp = db.session.execute(db.select(Chamada)).scalars().all()

#     return jsonify(resp)