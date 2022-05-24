from flask import Flask
from .routes.usuario import clientes
from .extentions import database
from .commands.userCommands import userCommands


def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb+srv://robson:<password>@cloudopss.ugxyu.mongodb.net/?retryWrites=true&w=majority"
    app.register_blueprint(clientes)
    app.register_blueprint(userCommands)
    database.init_app(app)


    return app


