import site
from os.path import dirname
site.addsitedir(dirname(__file__))

from flask import Flask
from extensions import db
import routes

def create_app():
    app = Flask(__name__)
    
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flask_user:password@localhost/flask_db'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    
    db.init_app(app)

    app.register_blueprint(routes.main_bp)
    
    app.register_blueprint(routes.api_bp,url_prefix='/api')

    with app.app_context():
        db.create_all()

    from .create_data import create_data
    create_data(app,db)

    return app