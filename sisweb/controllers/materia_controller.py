from models.materia import MateriaModel

class MateriaController:
    def __init__(self):
        self.model = MateriaModel()

    def listar(self):
        return self.model.listar()