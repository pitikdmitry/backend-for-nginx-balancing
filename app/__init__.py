from flask import Flask

from config import app_config
from app.blueprints.users_blueprint import users_blueprint


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    app.register_blueprint(users_blueprint, url_prefix='/users')

    return app
