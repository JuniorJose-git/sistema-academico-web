from flask import Blueprint

from ..extensions import db
from ..models.tipo_responsavel import TipoResponsavel

tipo_responsavel = Blueprint('tipo_responsavel', __name__)

# @tipo_responsavel.route('/tipo-resp')
# def create_tipo_responsavel():
#     db.create_all()

#     return "tipo_responsavel"
