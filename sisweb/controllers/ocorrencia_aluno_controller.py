from models.ocorrencia_aluno import OcorrenciaAlunoModel

class OcorrenciaAlunoController:
    def __init__(self):
        self.model = OcorrenciaAlunoModel()

    def listar(self):
        return self.model.listar()