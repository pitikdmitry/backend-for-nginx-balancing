import statsd
from flask import Blueprint, request, make_response, jsonify

from app.repositories.users_repository import UsersRepository

users_blueprint_obj = Blueprint('users', __name__)
users_repository = UsersRepository()
c = statsd.StatsClient('95.213.200.95', 8125, prefix='backend1')

STATUS_CODE = {
    'OK': 200,
    'CREATED': 201,
    'NOT_FOUND': 404,
    'UNAUTHORIZED': 401,
    'CONFLICT': 409
}


def use_stats_d():
    c.incr('backend1')


@users_blueprint_obj.route('/create', methods=['POST'])
def create_echo():
    use_stats_d()
    data = request.data
    if data == b'':
        return make_response("", STATUS_CODE['UNAUTHORIZED'])

    status_code = users_repository.create(data)

    if status_code == STATUS_CODE['OK']:
        return data
    else:
        return make_response("", status_code)


@users_blueprint_obj.route('/', methods=['GET'])
def get_user():
    use_stats_d()

    status_code = STATUS_CODE.get("OK")

    if status_code == STATUS_CODE['OK']:
        return jsonify("HELLO!")
