from extensions import db
from dataclasses import dataclass

@dataclass
class SalaDeAula(db.Model):
    __tablename__ = "sala_de_aula"

    id: int = db.Column(db.Integer, primary_key=True)

    nome: str  = db.Column(db.String(100), nullable=False)

    capacidade: int  = db.Column(db.Integer, nullable=False)

    # ----------

    turma = db.relationship("Turma",back_populates="sala_de_aula")

class SalaDeAulaModel:
    def listar(self):
        return SalaDeAula.query.all()