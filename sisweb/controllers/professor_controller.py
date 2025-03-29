from models.professor import ProfessorModel

class ProfessorController:
    def __init__(self):
        self.model = ProfessorModel()

    def listar(self):
        return self.model.listar()