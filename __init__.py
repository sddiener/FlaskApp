from logging import debug
from flask import Flask, render_template, url_for
import random

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template("index.html")

@app.route("/projects", methods=['POST', 'GET'])
def projects():
    num = random.randint(1,6)
    return render_template("projects.html", random_number = num)

@app.route("/about", methods=['POST', 'GET'])
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host = "0.0.0.0", port = 5000)
