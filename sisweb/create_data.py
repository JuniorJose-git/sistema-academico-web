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

    #sala_de_aula

    create_data_sala_de_aula(app,db)

    #dia_semana

    create_data_dia_semana(app,db)

    #horario 

    create_data_horario(app,db)


    #dia_horario
    create_dia_horario(app,db)

    #materia

    create_data_materia(app,db)

    #diciplina

    create_data_disciplina(app,db)

    #turma e horario

    create_data_turma(app,db)


    #aluno_turma
    create_data_aluno_turma(app,db)


def create_data_aluno(app,db):
    from models.aluno import Aluno
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
    from models.responsavel import Responsavel

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
    from models.tipo_responsavel import TipoResponsavel
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
    from models.responsavel_aluno import ResponsavelAluno

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
    from models.serie import Serie

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
    from models.ano_escolar import AnoEscolar

    x = [
        AnoEscolar(nome='2025',data_inicio=date(2025,1,1),data_fim=date(2025,12,31)),
        AnoEscolar(nome='2024',data_inicio=date(2024,1,1),data_fim=date(2024,12,31))

    ]

    with app.app_context():

        resp = db.session.execute(db.select(AnoEscolar)).scalars().all()

        bol = True

        if len(resp) <= 0:
            db.session.add_all(x)
            db.session.commit()
    

def create_data_serie_aluno(app,db):
    from models.serie_aluno import SerieAluno
    x = [
        SerieAluno(id_aluno=1, id_serie=1, id_ano_escolar=1),
        SerieAluno(id_aluno=2, id_serie=1, id_ano_escolar=1),
        SerieAluno(id_aluno=3, id_serie=1, id_ano_escolar=1),
        SerieAluno(id_aluno=4, id_serie=1, id_ano_escolar=1),
        SerieAluno(id_aluno=5, id_serie=1, id_ano_escolar=1),
    ]

    with app.app_context():

        resp = db.session.execute(db.select(SerieAluno)).scalars().all()

        if len(resp) <= 0:
            db.session.add_all(x)
            db.session.commit()


def create_data_periodo(app, db):
    from models.periodo import Periodo
    x = [
        Periodo(numero_periodo=1, data_inicio=date(2025, 1, 1), data_fim=date(2025, 3, 31), id_ano_escolar=1),
        Periodo(numero_periodo=2, data_inicio=date(2025, 4, 1), data_fim=date(2025, 6, 30), id_ano_escolar=1),
        Periodo(numero_periodo=3, data_inicio=date(2025, 7, 1), data_fim=date(2025, 9, 30), id_ano_escolar=1),
        Periodo(numero_periodo=4, data_inicio=date(2025, 10, 1), data_fim=date(2025, 12, 31), id_ano_escolar=1),
        Periodo(numero_periodo=1, data_inicio=date(2024, 1, 1), data_fim=date(2024, 3, 31), id_ano_escolar=2),
        Periodo(numero_periodo=2, data_inicio=date(2024, 4, 1), data_fim=date(2024, 6, 30), id_ano_escolar=2),
        Periodo(numero_periodo=3, data_inicio=date(2024, 7, 1), data_fim=date(2024, 9, 30), id_ano_escolar=2),
        Periodo(numero_periodo=4, data_inicio=date(2024, 10, 1), data_fim=date(2024, 12, 31), id_ano_escolar=2),
    ]
    
    with app.app_context():

        resp = db.session.execute(db.select(Periodo)).scalars().all()

        if len(resp) <= 0:
            db.session.add_all(x)
            db.session.commit()


def create_data_professor(app,db):
    from models.professor import Professor

    x = [
        Professor(nome='Pedro Almeida',cpf='12345678901',email='pedro.almeida@email.com',senha='senha123',telefone='11912345678',genero='Masculino'),
        Professor(nome='Cláudia Lima',cpf='98765432100',email='claudia.lima@email.com',senha='senha456',telefone='11923456789',genero='Feminino'),
        Professor(nome='Mariana Oliveira', cpf='11122233344', email='mariana.oliveira@email.com', senha='senha123', telefone='11987654321', genero='Feminino'),
        Professor(nome='Ricardo Santos', cpf='22233344455', email='ricardo.santos@email.com', senha='senha456', telefone='11976543210', genero='Masculino'),
        Professor(nome='Fernanda Costa', cpf='33344455566', email='fernanda.costa@email.com', senha='senha789', telefone='11965432109', genero='Feminino'),
        Professor(nome='Gustavo Almeida', cpf='44455566677', email='gustavo.almeida@email.com', senha='senha321', telefone='11954321098', genero='Masculino'),
        Professor(nome='Laura Mendes', cpf='55566677788', email='laura.mendes@email.com', senha='senha654', telefone='11943210987', genero='Feminino'),
        Professor(nome='Carlos Henrique', cpf='66677788899', email='carlos.henrique@email.com', senha='senha987', telefone='11932109876', genero='Masculino'),
        Professor(nome='Vanessa Lima', cpf='77788899900', email='vanessa.lima@email.com', senha='senha147', telefone='11921098765', genero='Feminino'),
        Professor(nome='Tiago Souza', cpf='88899900011', email='tiago.souza@email.com', senha='senha258', telefone='11910987654', genero='Masculino'),
        Professor(nome='Patrícia Rocha', cpf='99900011122', email='patricia.rocha@email.com', senha='senha369', telefone='11909876543', genero='Feminino'),
        Professor(nome='Eduardo Martins', cpf='00011122233', email='eduardo.martins@email.com', senha='senha159', telefone='11908765432', genero='Masculino')
    ]

    with app.app_context():

        resp = db.session.execute(db.select(Professor)).scalars().all()

        if len(resp) <= 0:
            db.session.add_all(x)
            db.session.commit()


def create_data_sala_de_aula(app,db):
    from models.sala_de_aula import SalaDeAula

    x = [
        SalaDeAula(nome='Sala 101',capacidade=30),
        SalaDeAula(nome='Sala 102',capacidade=20),
        SalaDeAula(nome='Sala 103',capacidade=35),
        SalaDeAula(nome='Sala 104',capacidade=30),
        SalaDeAula(nome='Sala 105',capacidade=40),
        SalaDeAula(nome='Sala 106',capacidade=30)
    ]

    with app.app_context():

        resp = db.session.execute(db.select(SalaDeAula)).scalars().all()

        if len(resp) <= 0:
            db.session.add_all(x)
            db.session.commit()


def create_data_dia_semana(app,db):
    from models.dia_semana import DiaSemana

    x = [
        DiaSemana(nome='Domingo',numero=1),
        DiaSemana(nome='Segunda-feira',numero=2),
        DiaSemana(nome='Terça-feira',numero=3),
        DiaSemana(nome='Quarta-feira',numero=4),
        DiaSemana(nome='Quinta-feira',numero=5),
        DiaSemana(nome='Sexta-feira',numero=6),
        DiaSemana(nome='Sábado',numero=7),

    ]

    with app.app_context():

        resp = db.session.execute(db.select(DiaSemana)).scalars().all()

        if len(resp) <= 0:
            db.session.add_all(x)
            db.session.commit()

def create_data_horario(app,db):
    from models.horario import Horario
    from datetime import time

    x = [
        Horario(
            nome="1º Período",
            horario_inicio=time.fromisoformat('07:00'),
            horario_fim=time.fromisoformat('09:00')
        ),
        Horario(
            nome="Intervalo",
            horario_inicio=time.fromisoformat('09:00'),
            horario_fim=time.fromisoformat('09:15')
        ),
        Horario(
            nome="2º Período",
            horario_inicio=time.fromisoformat('09:15'),
            horario_fim=time.fromisoformat('11:15')
        )

    ]

    with app.app_context():

        resp = db.session.execute(db.select(Horario)).scalars().all()

        if len(resp) <= 0:
            db.session.add_all(x)
            db.session.commit()


def create_dia_horario(app,db):
    from models.dia_horario import DiaHorario
    from models.horario import Horario
    from models.dia_semana import DiaSemana

    with app.app_context(): 
        dia_semana = db.session.execute(db.select(DiaSemana)).scalars().all()

    with app.app_context(): 
        horarios = db.session.execute(db.select(Horario)).scalars().all()

    x = list()
        
    for dia in dia_semana:
        for horario in horarios:
            x.append(DiaHorario(id_horario=horario.id,id_dia_semana=dia.id))
    


    with app.app_context():

        resp = db.session.execute(db.select(DiaHorario)).scalars().all()

        if len(resp) <= 0:
            db.session.add_all(x)
            db.session.commit()


def create_data_materia(app,db):
    from models.materia import Materia

    x = [
        Materia(nome="Matemática", descricao="Estudo dos números, formas, funções e equações."),
        Materia(nome="Física", descricao="Análise das forças, movimento, energia e matéria."),
        Materia(nome="Química", descricao="Estudo da composição, estrutura e propriedades da matéria."),
        Materia(nome="Biologia", descricao="Ciência que estuda os seres vivos e seus processos vitais."),
        Materia(nome="História", descricao="Análise dos eventos passados e sua influência no presente."),
        Materia(nome="Geografia", descricao="Estudo da Terra, suas paisagens, população e fenômenos."),
        Materia(nome="Português", descricao="Língua portuguesa, gramática, literatura e redação."),
        Materia(nome="Inglês", descricao="Estudo da língua inglesa e suas aplicações."),
        Materia(nome="Filosofia", descricao="Reflexão sobre questões fundamentais da existência humana."),
        Materia(nome="Sociologia", descricao="Análise das estruturas e relações sociais."),
        Materia(nome="Educação Física", descricao="Prática e estudo do corpo e atividades físicas."),
        Materia(nome="Artes", descricao="Expressão artística, estética e história da arte."),
    ]

    with app.app_context():

        resp = db.session.execute(db.select(Materia)).scalars().all()

        if len(resp) <= 0:
            db.session.add_all(x)
            db.session.commit()


def create_data_disciplina(app,db):

    from models.materia import Materia
    from models.disciplina import Disciplina

    with app.app_context(): 
        materias = db.session.execute(db.select(Materia)).scalars().all()

    x = list()

    map_disci = {
        "Matemática": ["Álgebra", "Geometria", "Trigonometria", "Estatística"],
        "Física": ["Mecânica", "Termodinâmica", "Eletromagnetismo", "Óptica"],
        "Química": ["Química Orgânica", "Química Inorgânica", "Fisico-Química", "Bioquímica"],
        "Biologia": ["Genética", "Ecologia", "Fisiologia", "Microbiologia"],
        "História": ["História Antiga", "História Medieval", "História Moderna", "História Contemporânea"],
        "Geografia": ["Geografia Física", "Geografia Humana", "Cartografia", "Geopolítica"],
        "Português": ["Gramática", "Literatura", "Produção Textual", "Interpretação de Texto"],
        "Inglês": ["Gramática Inglesa", "Compreensão Oral", "Leitura e Escrita", "Conversação"],
        "Filosofia": ["Filosofia Antiga", "Filosofia Medieval", "Filosofia Moderna", "Ética e Moral"],
        "Sociologia": ["Sociologia Geral", "Política e Sociedade", "Cultura e Identidade", "Movimentos Sociais"],
        "Educação Física": ["Esportes Coletivos", "Treinamento Físico", "Saúde e Bem-estar", "Anatomia do Exercício"],
        "Artes": ["História da Arte", "Música", "Teatro", "Artes Visuais"],
    }

    for materia in materias:
        for disciplina in map_disci[materia.nome]:
            x.append(Disciplina(
                nome=disciplina,
                descricao=f"Disciplina relacionada à matéria de {materia.nome}.",
                id_materia=materia.id))
        
    with app.app_context():

        resp = db.session.execute(db.select(Disciplina)).scalars().all()

        if len(resp) <= 0:
            db.session.add_all(x)
            db.session.commit()


def create_data_turma(app, db):
    from models.turma import Turma
    from models.professor import Professor
    from models.sala_de_aula import SalaDeAula
    from models.disciplina import Disciplina
    from models.materia import Materia

    x = []

    with app.app_context():
        professores = db.session.execute(db.select(Professor)).scalars().all()
        materias = db.session.execute(db.select(Materia)).scalars().all()
        salas = db.session.execute(db.select(SalaDeAula)).scalars().all()


        for i, materia in enumerate(materias):
            for j, disciplina in enumerate(materia.disciplina):
                x.append(Turma(
                    id_disciplina=disciplina.id,
                    id_professor=(i+1),
                    id_sala_de_aula=salas[i % len(salas)].id,
                    id_periodo=(j+1),
                ))
                

    x.append(Turma(
        id_disciplina=1,
        id_professor=1,
        id_sala_de_aula=1,
        id_periodo=5,
        ))

    with app.app_context():
        if not db.session.execute(db.select(Turma)).scalars().all():
            db.session.add_all(x)
            db.session.commit()




# def create_data_turma(app, db):
#     from models.turma import Turma
#     from models.professor import Professor
#     from models.sala_de_aula import SalaDeAula
#     from models.periodo import Periodo
#     from models.disciplina import Disciplina
#     from models.turma_dia_horario import TurmaDiaHorario
#     from models.dia_horario import DiaHorario

#     with app.app_context():
#         professores = db.session.execute(db.select(Professor)).scalars().all()
#         salas = db.session.execute(db.select(SalaDeAula)).scalars().all()
#         periodos = db.session.execute(db.select(Periodo)).scalars().all()
#         disciplinas = db.session.execute(db.select(Disciplina)).scalars().all()
#         dia_horarios = db.session.execute(db.select(DiaHorario)).scalars().all()
    
#     turmas = []
    
#     for i in range(5):
#         turma = Turma(
#             id_disciplina=disciplinas[i % len(disciplinas)].id,
#             id_professor=professores[i % len(professores)].id,
#             id_sala_de_aula=salas[i % len(salas)].id,
#             id_periodo=periodos[i % len(periodos)].id
#         )
#         turmas.append(turma)
    
#     with app.app_context():
#         if not db.session.execute(db.select(Turma)).scalars().all():
#             db.session.add_all(turmas)
#             db.session.commit()
    
#     with app.app_context():
#         turmas = db.session.execute(db.select(Turma)).scalars().all()
    
#     turma_dia_horarios = []
    
#     for i, turma in enumerate(turmas):
#         for j in range(3):  # 3 horários por turma
#             dia_horario = dia_horarios[(i * 3 + j) % len(dia_horarios)]
#             turma_dia_horarios.append(TurmaDiaHorario(
#                 id_turma=turma.id,
#                 id_dia_horario=dia_horario.id
#             ))
    
#     with app.app_context():
#         if not db.session.execute(db.select(TurmaDiaHorario)).scalars().all():
#             db.session.add_all(turma_dia_horarios)
#             db.session.commit()


def create_data_aluno_turma(app,db):
    from models.turma import Turma
    from models.aluno import Aluno
    from models.aluno_turma import AlunoTurma


    with app.app_context():
        turmas = db.session.execute(db.select(Turma)).scalars().all()
        alunos = db.session.execute(db.select(Aluno)).scalars().all()

        # for aluno in alunos:
        #     print(f"{aluno.nome} {aluno.id} = {aluno.serie_aluno.serie.nome}")

        # for turma in turmas:
        #     if (turma.id == 1):
        #         for aluno in turma.aluno_turma:
        #             print(f"{aluno.aluno.nome} {aluno.aluno.serie_aluno.serie.nome}")

    x = [
        AlunoTurma(id_aluno=1,id_turma=1,nota=30),
        AlunoTurma(id_aluno=1,id_turma=2,nota=23),
        AlunoTurma(id_aluno=1,id_turma=3,nota=34),
        AlunoTurma(id_aluno=1,id_turma=4,nota=12),
        AlunoTurma(id_aluno=1,id_turma=5,nota=34),
        AlunoTurma(id_aluno=1,id_turma=6,nota=45),
        AlunoTurma(id_aluno=1,id_turma=7,nota=50),
        AlunoTurma(id_aluno=1,id_turma=8,nota=56),
        AlunoTurma(id_aluno=2,id_turma=1,nota=60),
        AlunoTurma(id_aluno=2,id_turma=2,nota=40),
        AlunoTurma(id_aluno=2,id_turma=3,nota=59),
        AlunoTurma(id_aluno=2,id_turma=4,nota=59),
        AlunoTurma(id_aluno=2,id_turma=5,nota=34),
        AlunoTurma(id_aluno=2,id_turma=6,nota=45),
        AlunoTurma(id_aluno=2,id_turma=7,nota=50),
        AlunoTurma(id_aluno=2,id_turma=8,nota=56),
        AlunoTurma(id_aluno=1,id_turma=1,nota=100),


    ]


    # x = [
    #     AlunoTurma(id_aluno=alunos[0].id,id_turma=turmas[0].id,nota=30),
    #     AlunoTurma(id_aluno=alunos[1].id,id_turma=turmas[1].id,nota=40),
    #     AlunoTurma(id_aluno=alunos[2].id,id_turma=turmas[2].id,nota=23),
    #     AlunoTurma(id_aluno=alunos[3].id,id_turma=turmas[0].id,nota=32),
    #     AlunoTurma(id_aluno=alunos[4].id,id_turma=turmas[1].id,nota=43)
    # ]
    
    with app.app_context():

        resp = db.session.execute(db.select(AlunoTurma)).scalars().all()

        if len(resp) <= 0:
            db.session.add_all(x)
            db.session.commit()