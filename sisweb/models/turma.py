from extensions import db
from dataclasses import dataclass

@dataclass
class Turma (db.Model):
    __tablename__ = "turma"
    id: int = db.Column(db.Integer, primary_key=True)
    
    id_disciplina: int = db.Column(db.ForeignKey("disciplina.id"), nullable=False)

    id_professor: int = db.Column(db.ForeignKey("professor.id"), nullable=False)

    id_sala_de_aula: int = db.Column(db.ForeignKey("sala_de_aula.id"), nullable=False)

    id_periodo: int = db.Column(db.ForeignKey("periodo.id"), nullable=False)


    # -------------

    disciplina = db.relationship("Disciplina",back_populates="turma")

    professor = db.relationship("Professor",back_populates="turma")

    sala_de_aula = db.relationship("SalaDeAula",back_populates="turma")

    periodo = db.relationship("Periodo",back_populates="turma")

    turma_dia_horario = db.relationship("TurmaDiaHorario",back_populates="turma")

    aluno_turma = db.relationship("AlunoTurma",back_populates="turma")



