from models.responsavel import ResponsavelModel

class ResponsavelController:
    def __init__(self):
        self.model = ResponsavelModel()

    def listar(self):
        return self.model.listar()