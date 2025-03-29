from models.serie_aluno import SerieAlunoModel

class SerieAlunoController:
    def __init__(self):
        self.model = SerieAlunoModel()

    def listar(self):
        return self.model.listar()