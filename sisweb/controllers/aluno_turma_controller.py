
from models.aluno_turma import AlunoTurmaModel

class AlunoTurmaController:
    def __init__(self):
        self.model = AlunoTurmaModel()

    def listar(self):
        return self.model.listar()