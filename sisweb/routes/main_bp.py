from flask import Blueprint

main_bp = Blueprint('main_bp', __name__)

import controllers

@main_bp.route("/")
def main():    

    alunocontroller = controllers.AlunoController()

    print(alunocontroller.listar())

    return "teste"