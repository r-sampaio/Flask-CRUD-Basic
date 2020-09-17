from app import app


@app.route("/hello")
def ola():
    return "Hello, Flask!"
