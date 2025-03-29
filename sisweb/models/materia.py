from extensions import db
from dataclasses import dataclass

@dataclass
class Materia(db.Model):
    __tablename__ = "materia"

    id: int = db.Column(db.Integer, primary_key=True)

    nome: str  = db.Column(db.String(100), nullable=False)

    descricao: str  = db.Column(db.String(200), nullable=False)

    # ----------


    disciplina = db.relationship("Disciplina",back_populates="materia")

class MateriaModel:
    def listar(self):
        return Materia.query.all()