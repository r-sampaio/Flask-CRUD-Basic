from app.models import cliente_model
from app import db


def listar_clientes():
    clientes = cliente_model.Cliente.query.all()
    return clientes

def list_clientes(id):
    cliente = cliente_model.Cliente.query.filter_by(id=id).first()
    return cliente

def cadastrat_cliente(cliente):
    db.session.add(cliente)
    db.session.commit()

def editar_cliente(cliente_db, cliente_novo):
    cliente_db.nome = cliente_novo.nome
    cliente_db.email = cliente_novo.email
    cliente_db.data_nascimento = cliente_novo.data_nascimento
    cliente_db.profissao = cliente_novo.profissao
    cliente_db.sexo = cliente_novo.sexo
    db.session.commit()

def remover_cliente(cliente):
    db.session.delete(cliente)
    db.session.commit()
    