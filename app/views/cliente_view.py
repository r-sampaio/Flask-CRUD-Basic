from flask import render_template
from app.forms import cliente_form
from app import app

# @app.route("/hello/", defaults={'nome': None})
# @app.route("/hello/<string:nome>")
# def teste(nome):
#     return render_template("clientes/teste.html", nome_usuario=nome)

# @app.route("/world")
# def world():
#     return "Hello World!"


@app.route("/cadastrar_cliente")
def cadastrar_cliente():
    form = cliente_form.ClienteForm()
    
    return render_template("cliente/form.html", form=form)
