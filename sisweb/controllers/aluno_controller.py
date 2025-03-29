
from models.aluno import AlunoModel

class AlunoController:
    def __init__(self):
        self.model = AlunoModel()

    def listar(self):
        return self.model.listar()
