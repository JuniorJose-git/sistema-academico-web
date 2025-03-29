from models.ocorrencia import OcorrenciaModel

class OcorrenciaController:
    def __init__(self):
        self.model = OcorrenciaModel()

    def listar(self):
        return self.model.listar()