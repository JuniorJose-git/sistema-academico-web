
from models.ano_escolar import AnoEscolarModel

class AnoEscolarController:
    def __init__(self):
        self.model = AnoEscolarModel()

    def listar(self):
        return self.model.listar()
