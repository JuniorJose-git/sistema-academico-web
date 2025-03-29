from models.periodo import PeriodoModel

class PeriodoController:
    def __init__(self):
        self.model = PeriodoModel()

    def listar(self):
        return self.model.listar()