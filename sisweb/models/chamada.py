from ..extensions import db
from dataclasses import dataclass

@dataclass
class Chamada (db.Model):
    __tablename__ = "chamada"
    id: int = db.Column(db.Integer, primary_key=True)
    
    data_chamada: str = db.Column(db.Date, nullable=False)

    presensa: db.Mapped["Boolean"] = db.Column(db.Boolean,nullable=False)

    id_aluno_turma: str = db.Column(db.ForeignKey("aluno_turma.id"),nullable=False)

    # -------------

    aluno_turma = db.relationship("AlunoTurma",back_populates="chamada")