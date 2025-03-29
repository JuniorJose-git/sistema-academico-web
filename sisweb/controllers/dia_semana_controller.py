from models.dia_semana import DiaSemanaModel

class DiaSemanaController:
    def __init__(self):
        self.model = DiaSemanaModel()

    def listar(self):
        return self.model.listar()