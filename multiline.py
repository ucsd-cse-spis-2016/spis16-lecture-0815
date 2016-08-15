from flask import Flask
app = Flask(__name__)

@app.route("/en")
def hello():
    return '''
<style>
  p { padding: 0px; margin: 0px;}
</style>
<p>Hello SPIS 2016!</p>
<p>How are you this morning?</p>
<p style="margin-left: 40px;">I'm good</p>
'''

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
