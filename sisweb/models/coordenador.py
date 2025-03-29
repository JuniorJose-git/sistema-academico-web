from extensions import db
from dataclasses import dataclass

@dataclass
class Coordenador(db.Model):
    __tablename__ = "coordenador"

    id: int = db.Column(db.Integer, primary_key=True)

    nome: str  = db.Column(db.String(100), nullable=False)

    cpf: str  = db.Column(db.String(11), nullable=False, unique=True)

    email: str  = db.Column(db.String(100), nullable=False, unique=True)

    senha: str  = db.Column(db.String(100), nullable=False)

    telefone: str  = db.Column(db.String(12), nullable=False)

    genero: str = db.Column(db.String(12), nullable=False)

    # ----------

    ocorrencia = db.relationship("Ocorrencia",back_populates="coordenador")