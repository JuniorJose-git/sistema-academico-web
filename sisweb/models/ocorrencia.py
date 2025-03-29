from extensions import db
from dataclasses import dataclass

@dataclass
class Ocorrencia (db.Model):
    __tablename__ = "ocorrencia"
    id: int = db.Column(db.Integer, primary_key=True)
    
    data: str = db.Column(db.Date, nullable=False)

    descricao: str  = db.Column(db.String(200), nullable=False)

    id_coordenador: str = db.Column(db.ForeignKey("coordenador.id"),nullable=False)

    # -------------

    coordenador = db.relationship("Coordenador",back_populates="ocorrencia")

    ocorrencia_aluno = db.relationship("OcorrenciaAluno",back_populates="ocorrencia")

class OcorrenciaModel:
    def listar(self):
        return Ocorrencia.query.all()