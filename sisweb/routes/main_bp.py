from flask import Blueprint, render_template, jsonify

main_bp = Blueprint('main_bp', __name__)

# @main_bp.route("/")
# def main():    
#     return render_template("index.html")


from controllers import ProfessorController

professorController = ProfessorController()

@main_bp.route("/professor/<int:id>")
def professor_logado(id):

    resp = professorController.professor_get(id)

    return render_template("professor.html",professor=resp,id=id)

@main_bp.route("/professor/<int:id>/relatorios")
def professor_relatorios(id):

    prof = professorController.professor_get(id)

    turmas = professorController.listar_turmas(id)

    return render_template('relatorio.html', professor=prof,id=id,turmas=turmas)