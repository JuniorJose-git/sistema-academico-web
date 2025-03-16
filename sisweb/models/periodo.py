from ..extensions import db
from dataclasses import dataclass

@dataclass
class Periodo (db.Model):
    __tablename__ = "periodo"
    id: int = db.Column(db.Integer, primary_key=True)
    
    numero_periodo: int = db.Column(db.Integer, nullable=False)
    
    data_inicio: str = db.Column(db.Date, nullable=False)

    data_fim: str = db.Column(db.Date, nullable=False)

    id_ano_escolar: int = db.Column(db.ForeignKey("ano_escolar.id"), nullable=False)

    # -------------

    ano_escolar = db.relationship("AnoEscolar",back_populates="periodo")

    turma = db.relationship("Turma",back_populates="periodo")



