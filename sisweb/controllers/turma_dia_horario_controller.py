from models.turma_dia_horario import TurmaDiaHorarioModel

class TurmaDiaHorarioController:
    def __init__(self):
        self.model = TurmaDiaHorarioModel()

    def listar(self):
        return self.model.listar()