from ..extensions import db

class Responsavel(db.Model):
        
    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(100), nullable=False)

    cpf = db.Column(db.String(11), nullable=False, unique=True)

    email = db.Column(db.String(100), nullable=False, unique=True)

    senha = db.Column(db.String(100), nullable=False)

    telefone = db.Column(db.String(12), nullable=False)