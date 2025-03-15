from ..extensions import db

class TipoResponsavel(db.Model):
    __tablename__ = "tipo_responsavel"
    
    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(20), nullable=False)
