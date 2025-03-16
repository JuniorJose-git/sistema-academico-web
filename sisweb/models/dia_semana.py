from ..extensions import db
from dataclasses import dataclass

@dataclass
class DiaSemana(db.Model):
    __tablename__ = "dia_semana"

    id: int = db.Column(db.Integer, primary_key=True)

    nome: str  = db.Column(db.String(100), nullable=False)

    numero: int  = db.Column(db.Integer, nullable=False)

    # ----------

    dia_horario = db.relationship("DiaHorario",back_populates="dia_semana")
