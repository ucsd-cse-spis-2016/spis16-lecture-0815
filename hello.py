from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello SPIS 2016!"

if __name__ == "__main__":
    app.run(port=5000)
