from flask import Flask

from app.blueprints.users_blueprint import *


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.register_blueprint(users_blueprint_obj, url_prefix='/users')

    return app
