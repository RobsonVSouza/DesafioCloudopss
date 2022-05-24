from flask import Flask
from .routes.clientes import clientes


def create_app():
    app = Flask(__name__)
    app.register_blueprint(clientes)

    return app


