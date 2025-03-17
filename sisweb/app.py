from flask import Flask
from .extensions import db

def create_app():
    app = Flask(__name__)
    
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flask_user:password@localhost/flask_db'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    
    db.init_app(app)

    from .controllers.responsavel_controller import responsavel
    app.register_blueprint(responsavel)

    from .controllers.aluno_controller import aluno
    app.register_blueprint(aluno)

    from .controllers.tipo_responsavel_controller import tipo_responsavel
    app.register_blueprint(tipo_responsavel)

    from .controllers.responsavel_aluno_controller import responsavel_aluno
    app.register_blueprint(responsavel_aluno)

    from .controllers.serie_controller import serie
    app.register_blueprint(serie)

    from .controllers.ano_escolar_controller import ano_escolar
    app.register_blueprint(ano_escolar)

    from .controllers.serie_aluno_controller import serie_aluno
    app.register_blueprint(serie_aluno)

    from .controllers.periodo_controller import periodo
    app.register_blueprint(periodo)

    from .controllers.professor_controller import professor
    app.register_blueprint(professor)

    from .controllers.sala_de_aula_controller import sala_de_aula
    app.register_blueprint(sala_de_aula)

    from .controllers.dia_semana_controller import dia_semana
    app.register_blueprint(dia_semana)

    from .controllers.horario_controller import horario
    app.register_blueprint(horario)

    from .controllers.materia_controller import materia
    app.register_blueprint(materia)

    from .controllers.disciplina_controller import disciplina
    app.register_blueprint(disciplina)

    from .controllers.turma_controller import turma
    app.register_blueprint(turma)

    from .controllers.dia_horario_controller import dia_horario
    app.register_blueprint(dia_horario)

    from .controllers.turma_dia_horario_controller import turma_dia_horario
    app.register_blueprint(turma_dia_horario)

    from .controllers.aluno_turma_controller import aluno_turma
    app.register_blueprint(aluno_turma)

    from .controllers.chamada_controller import chamada
    app.register_blueprint(chamada)

    from .controllers.coordenador_controller import coordenador
    app.register_blueprint(coordenador)

    from .controllers.ocorrencia_controller import ocorrencia
    app.register_blueprint(ocorrencia)

    from .controllers.ocorrencia_aluno_controller import ocorrencia_aluno
    app.register_blueprint(ocorrencia_aluno)

    with app.app_context():
        db.create_all()

    from .create_data import create_data
    create_data(app,db)

    return app