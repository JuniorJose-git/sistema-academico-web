from extensions import db
from dataclasses import dataclass

@dataclass
class Responsavel(db.Model):
        
    id: int = db.Column(db.Integer, primary_key=True)

    nome: str  = db.Column(db.String(100), nullable=False)

    cpf: str  = db.Column(db.String(11), nullable=False, unique=True)

    email: str  = db.Column(db.String(100), nullable=False, unique=True)

    senha: str  = db.Column(db.String(100), nullable=False)

    telefone: str  = db.Column(db.String(12), nullable=False)
    

    # ----------

    responsavel_aluno = db.relationship("ResponsavelAluno", back_populates="responsavel")