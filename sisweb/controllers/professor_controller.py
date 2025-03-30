from models.professor import ProfessorModel

class ProfessorController:
    def __init__(self):
        self.model = ProfessorModel()

    def listar(self):
        return self.model.listar()


    def listar_turmas(self, id):
        return self.model.listar_turmas(id)

    def listar_turmas_ano(self, id, id_ano):
        return self.model.listar_turmas_ano(id, id_ano)

    def professor_get(self,id):
        return self.model.professor_get(id)

    def get_ano_escolar(self, id):
        return self.model.get_ano_escolar(id)

    def get_turma(self,id, id_turma):
        return self.model.get_turma(id, id_turma)