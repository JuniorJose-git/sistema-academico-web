from models.professor import ProfessorModel

class ProfessorController:
    def __init__(self):
        self.model = ProfessorModel()

    def listar(self):
        return self.model.listar()


    def listar_turmas(self, id):

        return self.model.listar_turmas(id)

    def professor_get(self,id):
        return self.model.professor_get(id)