from flask import Blueprint, request, jsonify
from ..services import example_service

bp = Blueprint('example', __name__)

@bp.route('/example', methods=['GET'])
def get_example():
    result = example_service.get_data()
    return jsonify(result)

@bp.route('/', methods= ['GET'])
def saludo():
    result = example_service.get_saludo()
    return jsonify(result)