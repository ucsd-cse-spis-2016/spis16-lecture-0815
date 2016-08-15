from flask import Flask
app = Flask(__name__)

@app.route("/en")
def hello():
    return "Hello SPIS 2016!"

@app.route("/cn")
def ni_hao():
    return "Ni Hao SPIS 2016!"

@app.route("/es")
def hola():
    return "Hola SPIS 2016!"

@app.route("/fa")
def sobh_bx():
    return "Sobh Bexair SPIS 2016!"

if __name__ == "__main__":
    app.run(port=5000)
