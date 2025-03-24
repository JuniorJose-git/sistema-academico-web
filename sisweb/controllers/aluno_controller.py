from flask import Blueprint, jsonify, render_template

from ..extensions import db
from ..models.aluno import Aluno
from ..models.materia import Materia
from ..models.aluno_turma import AlunoTurma
from sqlalchemy.sql import text


aluno = Blueprint('aluno', __name__)

@aluno.route("/aluno")
def aluno_json():
    aluno = db.session.execute(db.select(Aluno)).scalars().first()

    # aluno = Aluno.query.first()

    # print(aluno)

    # aluno_turmas = AlunoTurma.query.filter_by(id_aluno=aluno.id).distinct()

    materias = db.session.execute(text(f"select distinct m.nome, m.id from aluno_turma a join turma t on (t.id = a.id_turma) join disciplina d on (t.id_disciplina = d.id) join materia m on (m.id = d.id_materia) where id_aluno = {aluno.id}; ")).all()


    somas = []
    

    for materia in materias:
        soma = 0
        for aluno_turma in aluno.aluno_turma:
            if materia[1] == aluno_turma.turma.disciplina.id_materia:
                soma += aluno_turma.nota
        somas.append(soma/len(aluno.serie_aluno[0].ano_escolar.periodo))
            

    return render_template('index.html',aluno=aluno, materias=materias, somas=somas)