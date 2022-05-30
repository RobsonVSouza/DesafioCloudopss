from bson.objectid import ObjectId
from flask import Blueprint, render_template, request, session
from flask.helpers import flash, url_for
from werkzeug.utils import redirect
from ..extentions.database import mongo

produto = Blueprint("produto", __name__, url_prefix="/produtos")

@produto.route('/list')
def listProdutos():
    if "username" in session:
        produtos = mongo.db.produtos.find()
        return render_template("produtos/list.html", produtos=produtos)
    else:
        return redirect(url_for("usuario.index"))


@produto.route('/insert', methods=["GET", "POST"])
def insertProduto():
    if request.method == 'GET':
        return render_template("produtos/insert.html")
    else:
        nome = request.form.get('nome')
        quantidade = request.form.get('quantidade')
        preco = request.form.get('preco')
        categoria = request.form.get('categoria')
        estoque = request.form.get('estoque')

        if not nome:
            flash("Campo 'nome' é obrigatório")
        elif not quantidade:
            flash("Campo 'quantidade' é obrigatorio.")
        elif not preco:
            flash("Campo 'preco' é obrigatório.")
        elif not categoria:
            flash("Campo 'categoria' é obrigatório.")
        elif not estoque:
            flash("Campo 'estoque' é obrigatorio ")
        else:
            mongo.db.produtos.insert_one(
                {
                    "produto": nome,
                    "quantidade": quantidade,
                    "preco": preco,
                    "categoria": categoria,
                    "estoque": estoque,
                    "valor_total": (float(quantidade) * float(preco))
                }
            )
            flash('Produto criado com sucesso')
        return redirect(url_for("produto.listProdutos"))


@produto.route("/edit", methods=["GET", "POST"])
def editProduto():
    if request.method == "GET":
        idproduto = request.values.get("idproduto")

        if not idproduto:
            flash("Campo 'idproduto' é obrigatório.")
            return redirect(url_for("produto.listProduto"))
        else:
            idprod = mongo.db.produtos.find({"_id": ObjectId(idproduto)})
            produto = [i for i in idprod]
            estoques = set()
            produtos = mongo.db.produtos.find()
            for pr in produtos:
                estoques.add(pr['estoque'])
            return render_template(
                "produtos/edit.html", produto=produto, estoques=estoques
            )
    else:
        idproduto = request.form.get("idproduto")
        nome = request.form.get("nome", "")
        categoria = request.form.get("categoria", "")
        estoque = request.form.get("estoque", "")
        preco = request.form.get("preco", "")
        quantidade = request.form.get("quantidade", "")


        if not idproduto:
            flash("Campo 'idproduto' é obrigatório")
        elif not nome:
            flash("Campo 'nome' é obrigatório e deve ter no máximo 40 caracteres.")
        elif not quantidade:
            flash("Campo 'quantidade' é obrigatório e deve ser numérico.")
        elif not categoria:
            flash("Campo 'categoria' é obrigatório ou é inválido.")
        elif not preco:
            flash("Campo 'preco' é obrigatorio ")
        elif not estoque:
            flash("Campo obrigatorio")
        else:
            total = float(preco) * float(quantidade)
            update = mongo.db.produtos.update_many(
                {"_id": ObjectId(idproduto)},
                {
                    "$set": {
                        "produto": nome,
                        "quantidade": quantidade,
                        "preco": preco,
                        "categoria": categoria,
                        "estoque": estoque,
                        "valor_total": total,
                    }
                },
            )
            flash("Produto alterado com sucesso!")
        return redirect(url_for("produto.listProdutos"))

@produto.route("/delete")
def deleteProduto():
    idproduto = request.values.get("idproduto",)
    if not idproduto:
        flash("Campo 'idproduto' é obrigatório.")
    else:
        deleteProduto = mongo.db.produtos.delete_one({"_id": ObjectId(idproduto)})
        flash("Cliente deletado com sucesso")
    return redirect(url_for("produto.listProdutos"))
