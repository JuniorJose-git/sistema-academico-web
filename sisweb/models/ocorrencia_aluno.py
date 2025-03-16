from ..extensions import db
from dataclasses import dataclass

@dataclass
class OcorrenciaAluno (db.Model):
    __tablename__ = "ocorrencia_aluno"
    id: int = db.Column(db.Integer, primary_key=True)
    
    id_ocorrencia: int = db.Column(db.ForeignKey("ocorrencia.id"), nullable=False)

    id_aluno:int = db.Column(db.ForeignKey("aluno.id"), nullable=False)


    # -------------

    aluno = db.relationship("Aluno",back_populates="ocorrencia_aluno")

    ocorrencia = db.relationship("Ocorrencia",back_populates="ocorrencia_aluno")



