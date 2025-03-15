from ..extensions import db

class Aluno (db.Model):
    __tablename__ = "aluno"
    id = db.Column(db.Integer, primary_key=True)
    
    nome = db.Column(db.String(100), nullable=False)

    cpf = db.Column(db.String(11), nullable=False, unique=True)

    email = db.Column(db.String(100), nullable=False, unique=True)

    senha = db.Column(db.String(100), nullable=False)

    telefone = db.Column(db.String(12), nullable=False)

    genero = db.Column(db.String(12), nullable=False)

    data_nascimento = db.Column(db.DateTime, nullable=False)

    matricula = db.Column(db.Integer, nullable=False, unique=True)

    data_matricula = db.Column(db.DateTime, nullable=False)
