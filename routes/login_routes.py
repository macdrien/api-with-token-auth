from flask import Blueprint, request, Response, jsonify

from common.http_status_code import HTTPStatusCode
from services.login_services import LoginServices
from models.user_model import UserModel

login = Blueprint('login', __name__)

@login.route('/users', methods=['GET'])
def get_all():
    return jsonify(LoginServices.get_all()), HTTPStatusCode.OK.value

@login.route('/register', methods=['POST'])
def register_new_user():
    body = request.get_json()
    user_id = LoginServices.create_user(UserModel(email=body['email'], password=body['password']))
    return jsonify(user_id), HTTPStatusCode.CREATED.value

@login.route('/login', methods=['POST'])
def login_user():
    body = request.get_json()
    token = LoginServices.login(body)

    if token is not None:
        return jsonify(token), HTTPStatusCode.CREATED.value
    else:
        message = {'error': 'Email or password invalid'}
        return jsonify(message), HTTPStatusCode.BAD_REQUEST.value