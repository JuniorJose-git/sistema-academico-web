from ..extensions import db
from dataclasses import dataclass

@dataclass
class Aluno (db.Model):
    __tablename__ = "aluno"
    id: int = db.Column(db.Integer, primary_key=True)
    
    nome: str = db.Column(db.String(100), nullable=False)

    cpf: str = db.Column(db.String(11), nullable=False, unique=True)

    email: str = db.Column(db.String(100), nullable=False, unique=True)

    senha: str = db.Column(db.String(100), nullable=False)

    telefone: str = db.Column(db.String(12), nullable=False)

    genero: str = db.Column(db.String(12), nullable=False)

    data_nascimento: str = db.Column(db.DateTime, nullable=False)

    matricula: str = db.Column(db.Integer, nullable=False, unique=True)

    data_matricula: str = db.Column(db.DateTime, nullable=False)


    # -------------

    responsavel_aluno = db.relationship("ResponsavelAluno", back_populates="aluno")

    serie_aluno: db.Mapped[str] = db.relationship("SerieAluno",back_populates="aluno")

    aluno_turma = db.relationship("AlunoTurma",back_populates="aluno")

    ocorrencia_aluno = db.relationship("OcorrenciaAluno",back_populates="aluno")



