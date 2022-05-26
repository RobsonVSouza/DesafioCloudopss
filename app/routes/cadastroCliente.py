from bson.objectid import ObjectId
from flask import Blueprint, request, session, render_template, redirect, url_for, flash
from ..extentions.database import mongo


cadastroCliente = Blueprint('cadastroCliente', __name__)


@cadastroCliente.route('/list')
def listCliente():
    if "username" in session:
        clientes = mongo.db.clientes.find()
        return render_template("clientes/list.html", clientes=clientes)
    else:
        return redirect(url_for("usuario.index"))



@cadastroCliente.route('/insert', methods=["GET", "POST"])
def insertCliente():
    if request.method == 'GET':
        return render_template("cliente/insert.html")
    else:
        nome = request.form.get('nome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        endereco = request.form.get('endereco')
        profissao = request.form.get('profissao')

        if not nome:
            flash("Nome é obrigatorio")
        elif not email:
            flash("Email é obrigatorio")
        elif not telefone or not telefone.isdigit():
            flash("Telefone obrigatorio")
        elif not endereco:
            flash("Endereço é obrigatorio")
        elif not profissao:
            flash("Profissão é obrigatorio")
        else:
            mongo.db.clientes.insert_one({
                "nome": nome,
                "email": email,
                "telefone": telefone,
                "endereco": endereco,
                "profissao": profissao
            })
            flash("Cadastro com sucesso")

        return redirect(url_for("cliente.listCliente"))




@cadastroCliente.route('/edit', methods=["GET","POST"])
def editCliente():
    if request.method =="GET":
        idcliente = request.values.get("idCliente")

        if not idcliente:
            flash("Id de cliente obrigatorio")
            return redirect(url_for("cliente.listCliente"))
        else:
            idCli = mongo.db.clientes.find({"_id": ObjectId(idcliente)})
            cliente = [cli for cli in idCli]
            nomes = set()
            cliente = mongo.db.clientes.find()
            for p in cliente:
                nomes.add(p['nomes'])
            return render_template("cliente/edit.html,", cliente=cliente, nomes=nomes)
    else:
        idliente = request.form.get("idcliente")
        nome = request.form.get("nome")
        email = request.form.get("email")
        telefone = request.form.get("telefone")
        endereco = request.form.get("endereco")
        profissao = request.form.get("profissao")

        if not idliente:
            flash("Campo é obrigatorio")
        elif not nome:
            flash("Campo obrigatorio")
        elif not email:
            flash("Campo é obrigatorio")
        elif not telefone:
            flash("Campo obrigatorio")
        elif not endereco:
            flash("Campo obrigatorio")
        elif not profissao:
            flash("Campo obrigatorio")
        else:
            mongo.db.clientes.update({"id": ObjectId(idliente)},
                                     {
                                         "$set":{
                                             "nome": nome,
                                             "email": email,
                                             "telefone": telefone,
                                             "endereco": endereco,
                                             "profissao": profissao
                                         }
                                     })
            flash("Produtos alterados")
            return redirect(url_for("cliente/listCliente"))




@cadastroCliente.route('/delete')
def deleteCliente():
    idcliente = request.values.get("idcliente")
    if not idcliente:
        flash("Campo id é obrigatorio")
    else:
        mongo.db.clientes.delete_one({"_id":ObjectId(idcliente)})
        flash("cliente deletado")
    return redirect(url_for("cliente/listCliente"))
