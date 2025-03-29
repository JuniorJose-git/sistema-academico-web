from models.serie import SerieModel

class SerieController:
    def __init__(self):
        self.model = SerieModel()

    def listar(self):
        return self.model.listar()