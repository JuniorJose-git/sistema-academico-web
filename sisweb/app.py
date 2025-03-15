from flask import Flask
from .extensions import db
from .controllers.responsavel_controller import responsavel
from .controllers.aluno_controller import aluno
from .controllers.tipo_responsavel_controller import tipo_responsavel
from .controllers.responsavel_aluno_controller import responsavel_aluno



def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flask_user:password@localhost/flask_db'
    
    db.init_app(app)

    app.register_blueprint(responsavel)
    app.register_blueprint(aluno)
    app.register_blueprint(tipo_responsavel)
    app.register_blueprint(responsavel_aluno)

    with app.app_context():
        db.create_all()

    
    return app