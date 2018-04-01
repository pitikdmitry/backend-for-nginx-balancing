from flask import Flask

from app.blueprints import users_blueprint


def create_app():
    app = Flask(__name__)

    app.register_blueprint(users_blueprint, url_prefix='/users')
    return app
