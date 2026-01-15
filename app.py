import os

from flask import Flask, render_template

app = Flask(__name__, template_folder='.')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/buscar")
def buscar():
    return render_template("buscar.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "").lower() in {"1", "true", "yes"}
    app.run(host="0.0.0.0", port=port, debug=debug)

