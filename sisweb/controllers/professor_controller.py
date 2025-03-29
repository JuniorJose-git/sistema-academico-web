# from flask import Blueprint, jsonify, render_template

from extensions import db
from models.professor import Professor


# professor = Blueprint('professor', __name__)


# @professor.route("/professor")
# def professor_json():
#     resp = db.session.execute(db.select(Professor).filter_by(id=10)).scalars().first()

#     # resp = db.session.execute(text("select * from professor where id=10")).first()

#     return render_template('index.html',professor=resp)