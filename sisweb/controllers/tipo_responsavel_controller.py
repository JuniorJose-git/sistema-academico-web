from models.tipo_responsavel import TipoResponsavelModel

class TipoResponsavelController:
    def __init__(self):
        self.model = TipoResponsavelModel()

    def listar(self):
        return self.model.listar()