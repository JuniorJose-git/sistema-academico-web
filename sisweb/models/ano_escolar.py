from ..extensions import db

from dataclasses import dataclass

@dataclass
class AnoEscolar(db.Model):
    __tablename__ = "ano_escolar"
    
    id: str = db.Column(db.Integer, primary_key=True)

    nome: str = db.Column(db.String(20), nullable=False)

    data_inicio: str = db.Column(db.Date, nullable=False)

    data_fim: str = db.Column(db.Date, nullable=False)

    # ------------
    
    serie = db.relationship("SerieAluno",back_populates="ano_escolar")

    periodo = db.relationship("Periodo",back_populates="ano_escolar")

