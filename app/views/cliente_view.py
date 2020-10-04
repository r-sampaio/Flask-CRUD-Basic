from flask import render_template, redirect, url_for, request
from app.forms import cliente_form
from app import db

from app import app
from app.models import cliente_model

# @app.route("/hello/", defaults={'nome': None})
# @app.route("/hello/<string:nome>")
# def teste(nome):
#     return render_template("clientes/teste.html", nome_usuario=nome)

# @app.route("/world")
# def world():
#     return "Hello World!"


@app.route("/cadastrar_cliente", methods=["GET", "POST"])
def cadastrar_cliente():
    form = cliente_form.ClienteForm()
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        data_nascimento = form.data_nascimento.data
        profissao = form.profissao.data
        sexo = form.sexo.data
        
        cliente = cliente_model.Cliente(nome=nome, 
                                        email=email, 
                                        data_nascimento=data_nascimento, 
                                        profissao=profissao, 
                                        sexo=sexo)
        try:
            db.session.add(cliente)
            db.session.commit()
            return redirect(url_for("listar_clientes"))
        except:
            print("Cliente não cadastrado")
        
    return render_template("clientes/form.html", form=form)

@app.route("/listar_clientes", methods=["GET"])
def listar_clientes():
    clientes = cliente_model.Cliente.query.all()
    return render_template("clientes/lista_clientes.html", clientes=clientes)

@app.route("/listar_cliente/<int:id>")
def listar_cliente(id):
    cliente = cliente_model.Cliente.query.filter_by(id=id).first()
    
    return render_template("clientes/lista_cliente.html", cliente=cliente)

@app.route("/editar_cliente/<int:id>", methods=["POST", "GET"])
def editar_cliente(id):
    cliente = cliente_model.Cliente.query.filter_by(id=id).first()
    form = cliente_form.ClienteForm(obj=cliente)
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        data_nascimento = form.data_nascimento.data
        profissao = form.profissao.data
        sexo = form.sexo.data
        
        cliente.nome = nome
        cliente.email = email
        cliente.data_nascimento = data_nascimento
        cliente.profissao = profissao
        cliente.sexo = sexo
        
        try:
            db.session.commit()
            return redirect(url_for("listar_clientes"))
        except:
            print('O Cliente não foi editado')
        
    return render_template("clientes/form.html", form=form)

@app.route("/remover_cliente/<int:id>", methods=["POST", "GET"])
def remover_cliente(id):
    cliente = cliente_model.Cliente.query.filter_by(id=id).first()
    if request.method == "POST":
        try:
            db.session.delete(cliente)
            db.session.commit()
            return redirect(url_for("listar_clientes"))
        except:
            print("Erro ao remover o cliente")
    
    return render_template("clientes/remover_cliente.html", cliente=cliente)
