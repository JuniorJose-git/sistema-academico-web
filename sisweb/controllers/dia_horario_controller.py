from models.dia_horario import DiaHorarioModel

class DiaHorarioController:
    def __init__(self):
        self.model = DiaHorarioModel()

    def listar(self):
        return self.model.listar()