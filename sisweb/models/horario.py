from ..extensions import db
from dataclasses import dataclass

@dataclass
class Horario(db.Model):
    __tablename__ = "horario"

    id: int = db.Column(db.Integer, primary_key=True)

    nome: str  = db.Column(db.String(50), nullable=False)

    horario_inicio: str = db.Column(db.Time, nullable=False)

    horario_fim: str = db.Column(db.Time, nullable=False)


    # ----------

    dia_horario = db.relationship("DiaHorario",back_populates="horario")
