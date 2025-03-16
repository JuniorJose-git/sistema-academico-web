from ..extensions import db
from dataclasses import dataclass

@dataclass
class DiaHorario (db.Model):
    __tablename__ = "dia_horario"
    id: int = db.Column(db.Integer, primary_key=True)
    
    id_horario: int = db.Column(db.ForeignKey("horario.id"), nullable=False)

    id_dia_semana: int = db.Column(db.ForeignKey("dia_semana.id"), nullable=False)

    # -------------

    horario = db.relationship("Horario",back_populates="dia_horario")

    dia_semana = db.relationship("DiaSemana",back_populates="dia_horario")

    turma_dia_horario = db.relationship("TurmaDiaHorario",back_populates="dia_horario")


