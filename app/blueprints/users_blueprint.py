import statsd
from time import sleep
from flask import Blueprint, request, make_response, jsonify


users_blueprint_obj = Blueprint('users', __name__)
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

    sleep(0.5)
    return data


@users_blueprint_obj.route('/', methods=['GET'])
def get_user():
    use_stats_d()

    sleep(0.5)
    return jsonify("HELLO!")
