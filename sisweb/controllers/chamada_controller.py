from models.chamada import ChamadaModel

class ChamadaController:
    def __init__(self):
        self.model = ChamadaModel()

    def listar(self):
        return self.model.listar()