from flask import Blueprint


usuario = Blueprint("usuario", __name__)

@usuario.route('/')
def index():
    return "Index"

@usuario.route('/home')
def home():
    return "home"

@usuario.route("/login")
def login():
    return "login"

@usuario.route("/logout")
def logout():
    return "logout"
