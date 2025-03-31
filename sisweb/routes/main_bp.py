from flask import Blueprint, render_template, jsonify, request, redirect

main_bp = Blueprint('main_bp', __name__)

# @main_bp.route("/")
# def main():    
#     return render_template("index.html")



from controllers import ProfessorController

professorController = ProfessorController()

@main_bp.route("/")
def login():
    return render_template('login.html')

@main_bp.route("/professor" , methods=["POST"])
def login_request():

    form_email = request.form.get('email')
    form_senha = request.form.get('senha')

    professor = professorController.get_professor_by_email(form_email)

    if professor:

        if professor.senha == str(form_senha):
            return redirect("/professor/"+str(professor.id))
        else:
            return redirect('/')

    else:
        return redirect('/')


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

@main_bp.route('/professor/<int:id>/<int:tid>')
def professor_get_turma(id,tid):
    prof = professorController.professor_get(id)
    turma = professorController.get_turma(id, tid)
    return render_template('turma.html', professor=prof, id=id, turma=turma)