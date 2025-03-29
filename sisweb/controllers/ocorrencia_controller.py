# from flask import Blueprint, jsonify

from extensions import db
from models.ocorrencia import Ocorrencia


# ocorrencia = Blueprint('ocorrencia', __name__)

# @ocorrencia.route("/ocorrencia")
# def ocorrencia_json():
#     resp = db.session.execute(db.select(Ocorrencia)).scalars().all()

#     return jsonify(resp)