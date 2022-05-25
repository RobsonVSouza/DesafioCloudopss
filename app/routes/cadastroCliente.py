from flask import Blueprint, request, session, render_template, redirect, url_for, flash
from ..extentions.database import mongo


cadastroCliente = Blueprint('cadastroCliente', __name__)


@cadastroCliente.route('/list')
def listCadastro():
    return "list"

@cadastroCliente.route('/insert')
def insertCadastro():
    return "insert"

@cadastroCliente.route('/edit')
def editCadastro():
    return "edit"

@cadastroCliente.route('/delete')
def deleteCadastro():
    return "delete"

