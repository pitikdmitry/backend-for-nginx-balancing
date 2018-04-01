from flask import Blueprint, request, make_response, jsonify, json

from app.repositories.users_repository import UsersRepository

users_blueprint = Blueprint('users', __name__)
users_repository = UsersRepository()

STATUS_CODE = {
    'OK': 200,
    'CREATED': 201,
    'NOT_FOUND': 404,
    'UNAUTHORIZED': 401,
    'CONFLICT': 409
}


@users_blueprint.route('/create', methods=['POST'])
def create_echo():
    request2 = request
    data = request.data
    if data == b'':
        return make_response("", STATUS_CODE['UNAUTHORIZED'])

    # data = json.loads(bytes_data)
    status_code = users_repository.create(data)

    if status_code == STATUS_CODE['OK']:
        return data
    else:
        return make_response("", status_code)


@users_blueprint.route('/', methods=['GET'])
def get_user():

    status_code = STATUS_CODE.get("OK")

    if status_code == STATUS_CODE['OK']:
        return jsonify("HELLO!")
