from ..extensions import db
from dataclasses import dataclass

@dataclass
class AlunoTurma (db.Model):
    __tablename__ = "aluno_turma"
    id: int = db.Column(db.Integer, primary_key=True)

    id_turma: int = db.Column(db.ForeignKey("turma.id"), nullable=False)
    
    id_aluno:int = db.Column(db.ForeignKey("aluno.id"), nullable=False)

    nota: int = db.Column(db.Integer, nullable=False, default=0)


    # -------------

    aluno = db.relationship("Aluno",back_populates="aluno_turma")

    turma = db.relationship("Turma",back_populates="aluno_turma")

    chamada = db.relationship("Chamada",back_populates="aluno_turma")


