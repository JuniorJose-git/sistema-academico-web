from models.turma import TurmaModel

class TurmaController:
    def __init__(self):
        self.model = TurmaModel()

    def listar(self):
        return self.model.listar()