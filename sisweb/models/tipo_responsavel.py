from extensions import db

from dataclasses import dataclass

@dataclass
class TipoResponsavel(db.Model):
    __tablename__ = "tipo_responsavel"
    
    id: str = db.Column(db.Integer, primary_key=True)

    nome: str = db.Column(db.String(20), nullable=False)


    # ------------

    #responsavel: db.Mapped[list["ResponsavelAluno"]] = db.relationship("ResponsavelAluno", back_populates="tipo_responsavel")

    responsavel = db.relationship("ResponsavelAluno", back_populates="tipo_responsavel")

class TipoResponsavelModel:
    def listar(self):
        return TipoResponsavel.query.all()