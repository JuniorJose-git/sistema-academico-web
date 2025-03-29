from models.horario import HorarioModel

class HorarioController:
    def __init__(self):
        self.model = HorarioModel()

    def listar(self):
        return self.model.listar()