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
def create():
    bytes_data = request.data
    data = json.loads(bytes_data)

    status_code = users_repository.create(data)

    if status_code == STATUS_CODE['OK']:
        return jsonify(data)

    return make_response("", status_code)
# asdgedr