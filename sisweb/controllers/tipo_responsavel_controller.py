from flask import Blueprint, jsonify

from ..extensions import db
from ..models.tipo_responsavel import TipoResponsavel

tipo_responsavel = Blueprint('tipo_responsavel', __name__)

# @tipo_responsavel.route('/tipo-resp')
# def create_tipo_responsavel():
#     db.create_all()

#     return "tipo_responsavel"


@tipo_responsavel.route('/tipo-resp')
def tipo_responsavel_json():
    a = db.session.execute(db.select(TipoResponsavel)).scalars().all()

    return jsonify(a)