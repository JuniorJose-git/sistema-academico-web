from flask import Blueprint, jsonify

api_bp = Blueprint('api_bp', __name__)

import controllers


professorController = controllers.ProfessorController()

@api_bp.route('/professor')
def professor_listar():
    return jsonify(professorController.listar())


@api_bp.route('/professor/<int:id>/turmas')
def professor_turmas_listar(id):
    return jsonify(professorController.listar_turma(id))