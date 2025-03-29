from extensions import db
from dataclasses import dataclass

@dataclass
class TurmaDiaHorario (db.Model):
    __tablename__ = "turma_dia_horario"
    id: int = db.Column(db.Integer, primary_key=True)
    
    id_dia_horario: int = db.Column(db.ForeignKey("dia_horario.id"), nullable=False)

    id_turma: int = db.Column(db.ForeignKey("turma.id"), nullable=False)

    # -------------

    dia_horario = db.relationship("DiaHorario",back_populates="turma_dia_horario")

    turma = db.relationship("Turma",back_populates="turma_dia_horario")

class TurmaDiaHorarioModel:
    def listar(self):
        return TurmaDiaHorario.query.all()