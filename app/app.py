from flask import Flask
from .routes.usuario import usuario
from .routes.produto import produto
from .extentions import database
from .commands.userCommands import userCommands


def create_app(config_object="app.settings"):
    app = Flask(__name__)
    app.config.from_object(config_object)

    app.register_blueprint(usuario)
    app.register_blueprint(produto)

    app.register_blueprint(userCommands)
    database.init_app(app)

    return app


