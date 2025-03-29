from extensions import db

from dataclasses import dataclass

@dataclass
class ResponsavelAluno(db.Model):
    __tablename__ = "responsavel_aluno"
    
    id:int = db.Column(db.Integer, primary_key=True)

    id_aluno:int = db.Column(db.ForeignKey("aluno.id"), nullable=False)
    
    id_responsavel:int = db.Column(db.ForeignKey("responsavel.id"), nullable=False)

    id_tipo_responsavel:int = db.Column(db.ForeignKey("tipo_responsavel.id"), nullable=False)



    # -------------

    aluno = db.relationship("Aluno",back_populates="responsavel_aluno")

    responsavel = db.relationship("Responsavel", back_populates="responsavel_aluno")

    tipo_responsavel = db.relationship("TipoResponsavel", back_populates="responsavel")
    