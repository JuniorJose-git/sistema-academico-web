from extensions import db
from dataclasses import dataclass

@dataclass
class Serie (db.Model):
    __tablename__ = "serie"
    id: int = db.Column(db.Integer, primary_key=True)
    
    nome: str = db.Column(db.String(100), nullable=False)

    nivel: int = db.Column(db.Integer, nullable=False)


    # -------------

    serie_aluno = db.relationship("SerieAluno",back_populates="serie")

class SerieModel:
    def listar(self):
        return Serie.query.all()