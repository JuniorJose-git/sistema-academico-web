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
    disciplina: str 
    periodo: str
    sala_de_aula: str
    alunos: str

@dataclass
class professorAluno:
    id: int
    nome: str
    nota: int

class ProfessorModel:
    def listar(self):
        return Professor.query.all()

    def listar_turma(self, id):

        # turma = db.session.execute(db.select(Turma).filter_by(id_professor = id)).scalars().all()

        # print(turma[0].aluno_turma.)

        professor = db.session.execute(db.select(Professor).filter_by(id = id)).scalars().first()

        turmas = []

        for tu in professor.turma:

            alunos = []

            for tualuno in tu.aluno_turma:
                alunos.append(professorAluno(
                    id=tualuno.aluno.id,
                    nome=tualuno.aluno.nome,
                    nota=tualuno.nota,
                ))

            turmas.append(professorTurma(
                id = tu.id,
                disciplina = tu.disciplina,
                periodo = tu.periodo,
                sala_de_aula = tu.sala_de_aula,
                alunos = alunos
            ))

        return turmas

    def professor_get(self,id):
        return db.get_or_404(Professor, id)
