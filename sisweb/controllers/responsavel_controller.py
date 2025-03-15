from flask import Blueprint

from ..extensions import db
from ..models.responsavel import Responsavel


responsavel = Blueprint('responsavel', __name__)

# @responsavel.route('/responsavel/user')
# def responsavel():
#     db.create_all()

#     return "resposavel"