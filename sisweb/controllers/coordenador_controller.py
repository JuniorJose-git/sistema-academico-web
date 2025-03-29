from models.coordenador import CoordenadorModel

class CoordenadorController:
    def __init__(self):
        self.model = CoordenadorModel()

    def listar(self):
        return self.model.listar()
