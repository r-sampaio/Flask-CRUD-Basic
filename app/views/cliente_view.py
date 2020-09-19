from app import app

@app.route("/hello/")
@app.route("/hello/<string:nome>")
def ola(nome):
    return f"Hello, {nome}!"

@app.route("/world")
def world():
    return "Hello World!"
