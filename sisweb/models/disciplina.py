from ..extensions import db
from dataclasses import dataclass

@dataclass
class Disciplina(db.Model):
    __tablename__ = "disciplina"

    id: int = db.Column(db.Integer, primary_key=True)

    nome: str  = db.Column(db.String(100), nullable=False)

    descricao: str  = db.Column(db.String(200), nullable=False)

    id_materia: int = db.Column(db.ForeignKey("materia.id"), nullable=False)

    # ----------

    materia = db.relationship("Materia",back_populates="disciplina")

    turma = db.relationship("Turma",back_populates="disciplina")
