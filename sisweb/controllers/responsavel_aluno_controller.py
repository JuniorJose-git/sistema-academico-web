from models.responsavel_aluno import ResponsavelAlunoModel

class ResponsavelAlunoController:
    def __init__(self):
        self.model = ResponsavelAlunoModel()

    def listar(self):
        return self.model.listar()