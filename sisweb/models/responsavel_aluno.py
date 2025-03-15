from ..extensions import db

class ResponsavelAluno(db.Model):
    __tablename__ = "responsavel_aluno"
    
    id = db.Column(db.Integer, primary_key=True)

    id_aluno = db.Column(db.ForeignKey("aluno.id"), nullable=False)
    
    id_responsavel = db.Column(db.ForeignKey("responsavel.id"), nullable=False)

    id_tipo_responsavel = db.Column(db.ForeignKey("tipo_responsavel.id"), nullable=False)