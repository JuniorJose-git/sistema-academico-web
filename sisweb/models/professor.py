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


class ProfessorModel:
    def listar(self):
        return Professor.query.all()

    def listar_turma(self, id):

        turma = db.session.execute(db.select(Professor.turma).filter_by(id = id))

        print(turma)

        return db.get_or_404(Professor, id)

    def professor_get(self,id):
        return db.get_or_404(Professor, id)
