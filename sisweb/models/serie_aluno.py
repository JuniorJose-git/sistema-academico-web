from extensions import db
from dataclasses import dataclass

@dataclass
class SerieAluno (db.Model):
    __tablename__ = "serie_aluno"
    id: int = db.Column(db.Integer, primary_key=True)
    
    id_aluno: int = db.Column(db.ForeignKey("aluno.id"), nullable=False)

    id_serie: int = db.Column(db.ForeignKey("serie.id"), nullable=False)

    id_ano_escolar: int = db.Column(db.ForeignKey("ano_escolar.id"), nullable=False)



    # -------------


    aluno = db.relationship("Aluno",back_populates="serie_aluno")

    ano_escolar = db.relationship("AnoEscolar",back_populates="serie_aluno")

    serie = db.relationship("Serie",back_populates="serie_aluno")

