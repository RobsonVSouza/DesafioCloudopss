from flask import Blueprint, render_template


clientes = Blueprint("clientes",__name__)

@clientes.route('/')
def index():
    return "Index"

@clientes.route('/list')
def listClient():
    return "list"

@clientes.route("/insert")
def insertClient():
    return "insert"

@clientes.route("/edit")
def editClient():
    return "edit"

@clientes.route('/delete')
def deleteClient():
    return 'delete'