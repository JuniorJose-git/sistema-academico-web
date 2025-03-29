from models.sala_de_aula import SalaDeAulaModel

class SalaDeAulaController:
    def __init__(self):
        self.model = SalaDeAulaModel()

    def listar(self):
        return self.model.listar()