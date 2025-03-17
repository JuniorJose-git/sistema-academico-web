from datetime import datetime, date
from flask import Flask 

def create_data(app, db):

    # Alunos
    create_data_aluno(app,db)

    # Responsavel

    create_data_responsavel(app,db)
    
    # Tipo Responsavel
    
    create_data_tipo_responsavel(app,db)
    
    # responsavel_aluno

    create_data_responsavel_aluno(app,db)

    # serie
    
    create_data_serie(app,db)

    # ano escolar

    create_data_ano_escolar(app,db)

    # serie aluno

    create_data_serie_aluno(app,db)

    # periodo

    create_data_periodo(app,db)

    #professor

    create_data_professor(app,db)


def create_data_aluno(app,db):
    from .models.aluno import Aluno
    x = [
    Aluno(
        nome="Ana Souza",
        cpf="12345678901",
        email="ana.souza@email.com",
        senha="senha123",
        telefone="11987654321",
        genero="Feminino",
        data_nascimento=datetime(2000, 5, 15),
        matricula=2023001,
        data_matricula=datetime(2023, 2, 10)
    ),
    Aluno(
        nome="Bruno Lima",
        cpf="23456789012",
        email="bruno.lima@email.com",
        senha="senha456",
        telefone="11976543210",
        genero="Masculino",
        data_nascimento=datetime(1999, 8, 22),
        matricula=2023002,
        data_matricula=datetime(2023, 2, 12)
    ),
    Aluno(
        nome="Carlos Mendes",
        cpf="34567890123",
        email="carlos.mendes@email.com",
        senha="senha789",
        telefone="11965432109",
        genero="Masculino",
        data_nascimento=datetime(2001, 3, 10),
        matricula=2023003,
        data_matricula=datetime(2023, 2, 15)
    ),
    Aluno(
        nome="Daniela Castro",
        cpf="45678901234",
        email="daniela.castro@email.com",
        senha="senha321",
        telefone="11954321098",
        genero="Feminino",
        data_nascimento=datetime(2002, 11, 30),
        matricula=2023004,
        data_matricula=datetime(2023, 2, 18)
    ),
    Aluno(
        nome="Eduardo Ferreira",
        cpf="56789012345",
        email="eduardo.ferreira@email.com",
        senha="senha654",
        telefone="11943210987",
        genero="Masculino",
        data_nascimento=datetime(1998, 6, 5),
        matricula=2023005,
        data_matricula=datetime(2023, 2, 20)
    )]

    with app.app_context():

        resp = db.session.execute(db.select(Aluno)).scalars().all()

        if len(resp) <= 0:
            db.session.add_all(x)
            db.session.commit()

def create_data_responsavel(app,db):
    from .models.responsavel import Responsavel

    x = [
        Responsavel(nome='Paulo Silva',cpf='12312312300',email='paulo.silva@email.com',senha='senha123',telefone='11912345678'),
        Responsavel(nome='Ana Mendes',cpf='32132132100',email='ana.mendes@email.com',senha='senha456',telefone='11923456789')
    ]

    with app.app_context():

        resp = db.session.execute(db.select(Responsavel)).scalars().all()

        if len(resp) <= 0:
            db.session.add_all(x)
            db.session.commit()

def create_data_tipo_responsavel(app,db):
    from .models.tipo_responsavel import TipoResponsavel
    x = [
    TipoResponsavel(nome="Pai"),
    TipoResponsavel(nome="Mãe"),
    TipoResponsavel(nome="Avô/Avó"),
    TipoResponsavel(nome="Tio/Tia"),
    TipoResponsavel(nome="Responsável Legal")
    ]
    with app.app_context():

        resp = db.session.execute(db.select(TipoResponsavel)).scalars().all()

        if len(resp) <= 0:
            db.session.add_all(x)
            db.session.commit()

def create_data_responsavel_aluno(app,db):
    from .models.responsavel_aluno import ResponsavelAluno

    x = [
        ResponsavelAluno(id_aluno=1,id_responsavel=2,id_tipo_responsavel=2),
        ResponsavelAluno(id_aluno=1,id_responsavel=1,id_tipo_responsavel=1)
    ]

    with app.app_context():

        resp = db.session.execute(db.select(ResponsavelAluno)).scalars().all()

        if len(resp) <= 0:
            db.session.add_all(x)
            db.session.commit()


def create_data_serie(app,db):
    from .models.serie import Serie

    x = [
        Serie(
            nome="1º ano",
            nivel=1
        ),
        Serie(
            nome="2º ano",
            nivel=2
        ),
        Serie(
            nome="3º ano",
            nivel=3
        )
    ]
    with app.app_context():

        resp = db.session.execute(db.select(Serie)).scalars().all()

        if len(resp) <= 0:
            db.session.add_all(x)
            db.session.commit()


def create_data_ano_escolar(app,db):
    from .models.ano_escolar import AnoEscolar

    x = [
        AnoEscolar(nome='2025',data_inicio=date(2025,1,1),data_fim=date(2025,12,31))
    ]

    with app.app_context():

        resp = db.session.execute(db.select(AnoEscolar)).scalars().all()

        bol = True

        if len(resp) <= 0:
            db.session.add_all(x)
            db.session.commit()
    

def create_data_serie_aluno(app,db):
    from .models.serie_aluno import SerieAluno
    x = [
        SerieAluno(id_aluno=1, id_serie=1, id_ano_escolar=1),
        SerieAluno(id_aluno=2, id_serie=2, id_ano_escolar=1),
        SerieAluno(id_aluno=3, id_serie=3, id_ano_escolar=1),
        SerieAluno(id_aluno=4, id_serie=1, id_ano_escolar=1),
        SerieAluno(id_aluno=5, id_serie=2, id_ano_escolar=1),
    ]

    with app.app_context():

        resp = db.session.execute(db.select(SerieAluno)).scalars().all()

        if len(resp) <= 0:
            db.session.add_all(x)
            db.session.commit()


def create_data_periodo(app, db):
    from .models.periodo import Periodo
    x = [
        Periodo(numero_periodo=1, data_inicio=date(2025, 1, 1), data_fim=date(2025, 3, 31), id_ano_escolar=1),
        Periodo(numero_periodo=2, data_inicio=date(2025, 4, 1), data_fim=date(2025, 6, 30), id_ano_escolar=1),
        Periodo(numero_periodo=3, data_inicio=date(2025, 7, 1), data_fim=date(2025, 9, 30), id_ano_escolar=1),
        Periodo(numero_periodo=4, data_inicio=date(2025, 10, 1), data_fim=date(2025, 12, 31), id_ano_escolar=1),

    ]
    
    with app.app_context():

        resp = db.session.execute(db.select(Periodo)).scalars().all()

        if len(resp) <= 0:
            db.session.add_all(x)
            db.session.commit()


def create_data_professor(app,db):
    from .models.professor import Professor

    x = [
        Professor(nome='Pedro Almeida',cpf='12345678901',email='pedro.almeida@email.com',senha='senha123',telefone='11912345678',genero='Masculino'),
        Professor(nome='Cláudia Lima',cpf='98765432100',email='claudia.lima@email.com',senha='senha456',telefone='11923456789',genero='Feminino')
    ]

    with app.app_context():

        resp = db.session.execute(db.select(Professor)).scalars().all()

        if len(resp) <= 0:
            db.session.add_all(x)
            db.session.commit()