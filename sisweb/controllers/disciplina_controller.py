from models.disciplina import DisciplinaModel

class DisciplinaController:
    def __init__(self):
        self.model = DisciplinaModel()

    def listar(self):
        return self.model.listar()