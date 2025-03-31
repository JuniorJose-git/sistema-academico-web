from extensions import db
from dataclasses import dataclass

@dataclass
class Professor(db.Model):
    __tablename__ = "professor"

    id: int = db.Column(db.Integer, primary_key=True)

    nome: str  = db.Column(db.String(100), nullable=False)

    cpf: str  = db.Column(db.String(11), nullable=False, unique=True)

    email: str  = db.Column(db.String(100), nullable=False, unique=True)

    senha: str  = db.Column(db.String(100), nullable=False)

    telefone: str  = db.Column(db.String(12), nullable=False)

    genero: str = db.Column(db.String(12), nullable=False)

    # ----------

    turma = db.relationship("Turma",back_populates="professor")

@dataclass
class professorTurma:
    id: int
    nome: str
    disciplina: str 
    periodo: str
    sala_de_aula: str
    alunos: str
    media_notas: str

@dataclass
class professorAluno:
    id: int
    nome: str
    nota: int

class ProfessorModel:
    def listar(self):
        return Professor.query.all()

    def listar_turmas(self, id):

        # turma = db.session.execute(db.select(Turma).filter_by(id_professor = id)).scalars().all()

        # print(turma[0].aluno_turma.)

        professor = db.session.execute(db.select(Professor).filter_by(id = id)).scalars().first()

        turmas = []

        for tu in professor.turma:

            alunos = []

            media_notas = 0

            for tualuno in tu.aluno_turma:

                media_notas += tualuno.nota
                alunos.append(professorAluno(
                    id=tualuno.aluno.id,
                    nome=tualuno.aluno.nome,
                    nota=tualuno.nota,
                ))

            if len(tu.aluno_turma) != 0:
                media_notas = format(round(media_notas / len(tu.aluno_turma), 2)).replace('.',',')
            else:
                media_notas = ' - '

            turmas.append(professorTurma(
                id = tu.id,
                nome= tu.nome,
                disciplina = tu.disciplina,
                periodo = tu.periodo,
                sala_de_aula = tu.sala_de_aula,
                alunos = alunos,
                media_notas = media_notas 
            ))

        return turmas

    def listar_turmas_ano(self, id, id_ano):

        # turma = db.session.execute(db.select(Turma).filter_by(id_professor = id)).scalars().all()

        # print(turma[0].aluno_turma.)

        professor = db.session.execute(db.select(Professor).filter_by(id = id)).scalars().first()

        turmas = []

        for tu in professor.turma:

            alunos = []

            media_notas = 0


            if tu.periodo.ano_escolar.id == int(id_ano):
                for tualuno in tu.aluno_turma:

                    media_notas += tualuno.nota
                    alunos.append(professorAluno(
                        id=tualuno.aluno.id,
                        nome=tualuno.aluno.nome,
                        nota=tualuno.nota,
                    ))


                if len(tu.aluno_turma) != 0:
                    media_notas = format(round(media_notas / len(tu.aluno_turma), 2)).replace('.',',')
                else:
                    media_notas = ' - '

                turmas.append(professorTurma(
                    id = tu.id,
                    nome= tu.nome,
                    disciplina = tu.disciplina,
                    periodo = tu.periodo,
                    sala_de_aula = tu.sala_de_aula,
                    alunos = alunos,
                    media_notas = media_notas 
                ))

        return turmas
    

    def professor_get(self,id):
        return db.get_or_404(Professor, id)


    def get_ano_escolar(self, id):

        professor = db.session.execute(db.select(Professor).filter_by(id = id)).scalars().first()

        anos_escolar = []

        anos_escolar.append(professor.turma[0].periodo.ano_escolar)

        for turma in professor.turma:
            for a in anos_escolar:
                if a.id != turma.periodo.ano_escolar.id:
                    anos_escolar.append(turma.periodo.ano_escolar)


        return anos_escolar

    def get_turma(self, id, id_turma):

        professor = db.session.execute(db.select(Professor).filter_by(id = int(id))).scalars().first()
        
        turma = [turma for turma in professor.turma if turma.id == int(id_turma)]

        turma = turma[0]
        alunos = []

        media_notas = 0

        for tualuno in turma.aluno_turma:

            media_notas += tualuno.nota
            alunos.append(professorAluno(
                id=tualuno.aluno.id,
               nome=tualuno.aluno.nome,
                nota=tualuno.nota,
            ))

        if len(turma.aluno_turma) != 0:
            media_notas = format(round(media_notas / len(turma.aluno_turma), 2)).replace('.',',')
        else:
            media_notas = ' - '


        result = professorTurma(
                    id = turma.id,
                    nome= turma.nome,
                    disciplina = turma.disciplina,
                    periodo = turma.periodo,
                    sala_de_aula = turma.sala_de_aula,
                    alunos = alunos,
                    media_notas = media_notas)

        return result
    
    def get_professor_by_email(self,email):

        professor = db.session.execute(db.select(Professor).filter_by(email=email)).scalars().first()

        return professor



