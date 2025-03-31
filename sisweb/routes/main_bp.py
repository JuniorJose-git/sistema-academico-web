from flask import Blueprint, render_template, jsonify, request

main_bp = Blueprint('main_bp', __name__)

# @main_bp.route("/")
# def main():    
#     return render_template("index.html")



from controllers import ProfessorController

professorController = ProfessorController()

@main_bp.route("/")
def login():
    return render_template('login.html')

@main_bp.route("/professor")
def login_request():
        
    return 'logado'

@main_bp.route("/professor/<int:id>")
def professor_logado(id):

    resp = professorController.professor_get(id)

    return render_template("professor.html",professor=resp,id=id)

@main_bp.route("/professor/<int:id>/relatorios")
def professor_relatorios(id):

    prof = professorController.professor_get(id)

    turmas = professorController.listar_turmas(id)

    anos_escolar = professorController.get_ano_escolar(id)

    print(turmas)

    return render_template('relatorio.html', professor=prof,id=id,turmas=turmas,anos_escolar=anos_escolar)


@main_bp.route("/professor/<int:id>/relatorios", methods=["POST"])
def professor_relatorios_post(id):

    prof = professorController.professor_get(id)

    anos_escolar = professorController.get_ano_escolar(id)
    
    id_ano = request.form.get('ano')
    
    turmas = professorController.listar_turmas_ano(id,id_ano)

    return render_template('relatorio.html', professor=prof,id=id,turmas=turmas,anos_escolar=anos_escolar,id_ano=int(id_ano))