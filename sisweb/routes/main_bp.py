from flask import Blueprint, jsonify

main_bp = Blueprint('main_bp', __name__)

import controllers

@main_bp.route("/")
def main():    

    alunocontroller = controllers.AlunoController()

    return jsonify(alunocontroller.listar())