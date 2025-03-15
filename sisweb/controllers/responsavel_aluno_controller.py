from flask import Blueprint

from ..extensions import db
from ..models.responsavel_aluno import ResponsavelAluno


responsavel_aluno = Blueprint('responsavel_aluno', __name__)