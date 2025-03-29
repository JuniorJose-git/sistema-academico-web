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

    return render_template("professor.html",professor=resp)