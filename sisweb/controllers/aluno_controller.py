from flask import Blueprint

from ..extensions import db
from ..models.aluno import Aluno


aluno = Blueprint('aluno', __name__)

# @aluno.route("/")
# def create_aluno():
#     db.create_all()

#     return "aluno"