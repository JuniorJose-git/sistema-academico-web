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


    # from .models.aluno import Aluno
    # from datetime import datetime

    # alunos = [
    # Aluno(
    #     nome="Ana Souza",
    #     cpf="12345678901",
    #     email="ana.souza@email.com",
    #     senha="senha123",
    #     telefone="11987654321",
    #     genero="Feminino",
    #     data_nascimento=datetime(2000, 5, 15),
    #     matricula=2023001,
    #     data_matricula=datetime(2023, 2, 10)
    # ),
    # Aluno(
    #     nome="Bruno Lima",
    #     cpf="23456789012",
    #     email="bruno.lima@email.com",
    #     senha="senha456",
    #     telefone="11976543210",
    #     genero="Masculino",
    #     data_nascimento=datetime(1999, 8, 22),
    #     matricula=2023002,
    #     data_matricula=datetime(2023, 2, 12)
    # ),
    # Aluno(
    #     nome="Carlos Mendes",
    #     cpf="34567890123",
    #     email="carlos.mendes@email.com",
    #     senha="senha789",
    #     telefone="11965432109",
    #     genero="Masculino",
    #     data_nascimento=datetime(2001, 3, 10),
    #     matricula=2023003,
    #     data_matricula=datetime(2023, 2, 15)
    # ),
    # Aluno(
    #     nome="Daniela Castro",
    #     cpf="45678901234",
    #     email="daniela.castro@email.com",
    #     senha="senha321",
    #     telefone="11954321098",
    #     genero="Feminino",
    #     data_nascimento=datetime(2002, 11, 30),
    #     matricula=2023004,
    #     data_matricula=datetime(2023, 2, 18)
    # ),
    # Aluno(
    #     nome="Eduardo Ferreira",
    #     cpf="56789012345",
    #     email="eduardo.ferreira@email.com",
    #     senha="senha654",
    #     telefone="11943210987",
    #     genero="Masculino",
    #     data_nascimento=datetime(1998, 6, 5),
    #     matricula=2023005,
    #     data_matricula=datetime(2023, 2, 20)
    # )]


    # with app.app_context():
    #     db.session.add_all(alunos)
    #     db.session.commit()



    # from .models.responsavel import Responsavel
    # with app.app_context():
    #     db.session.add(Responsavel(nome='Paulo Silva',cpf='12312312300',email='paulo.silva@email.com',senha='senha123',telefone='11912345678'))
    #     db.session.add(Responsavel(nome='Ana Mendes',cpf='32132132100',email='ana.mendes@email.com',senha='senha456',telefone='11923456789'))
    #     db.session.commit()

    # from .models.tipo_responsavel import TipoResponsavel
    # tipos_responsaveis = [
    # TipoResponsavel(nome="Pai"),
    # TipoResponsavel(nome="Mãe"),
    # TipoResponsavel(nome="Avô/Avó"),
    # TipoResponsavel(nome="Tio/Tia"),
    # TipoResponsavel(nome="Responsável Legal")
    # ]
    # with app.app_context():
    #     db.session.add_all(tipos_responsaveis)
    #     db.session.commit()

    # from .models.responsavel_aluno import ResponsavelAluno

    # with app.app_context():

    #     responsavel = Responsavel(nome='Paulo Silva',cpf='12312312300',email='paulo.silva@email.com',senha='senha123',telefone='11912345678')

    #     db.session.add(ResponsavelAluno(aluno=alunos[0],responsavel=responsavel,tipo_responsavel=tipos_responsaveis[0]))

    #     db.session.add(ResponsavelAluno(id_aluno=1,id_responsavel=2,id_tipo_responsavel=2))
    #     db.session.add(ResponsavelAluno(id_aluno=1,id_responsavel=1,id_tipo_responsavel=1))



    #     db.session.commit()

    # from .models.serie import Serie
    # with app.app_context():
    #     series = [
    #         Serie(
    #             nome="1º ano",
    #             nivel=1
    #         ),
    #         Serie(
    #             nome="2º ano",
    #             nivel=2
    #         ),
    #         Serie(
    #             nome="3º ano",
    #             nivel=3
    #         )
    #     ]

    #     db.session.add_all(series)
    #     db.session.commit()

    # from datetime import date
    # from .models.ano_escolar import AnoEscolar
    # with app.app_context():
    #     db.session.add(AnoEscolar(nome='2025',data_inicio=date(2025,1,1),data_fim=date(2025,12,31)))
    #     db.session.commit()

    # from .models.serie_aluno import SerieAluno
    # serie_alunos = [
    #     SerieAluno(id_aluno=1, id_serie=1, id_ano_escolar=1),
    #     SerieAluno(id_aluno=2, id_serie=2, id_ano_escolar=1),
    #     SerieAluno(id_aluno=3, id_serie=3, id_ano_escolar=1),
    #     SerieAluno(id_aluno=4, id_serie=1, id_ano_escolar=1),
    #     SerieAluno(id_aluno=5, id_serie=2, id_ano_escolar=1),
    # ]

    # with app.app_context():
    #     db.session.add_all(serie_alunos)
    #     db.session.commit()

    # from .models.periodo import Periodo
    # from datetime import date
    # periodos = [
    #     Periodo(numero_periodo=1, data_inicio=date(2025, 1, 1), data_fim=date(2025, 3, 31), id_ano_escolar=1),
    #     Periodo(numero_periodo=2, data_inicio=date(2025, 4, 1), data_fim=date(2025, 6, 30), id_ano_escolar=1),
    #     Periodo(numero_periodo=3, data_inicio=date(2025, 7, 1), data_fim=date(2025, 9, 30), id_ano_escolar=1),
    #     Periodo(numero_periodo=4, data_inicio=date(2025, 10, 1), data_fim=date(2025, 12, 31), id_ano_escolar=1),

    # ]

    # with app.app_context():
    #     db.session.add_all(periodos)
    #     db.session.commit()

    return app