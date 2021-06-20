from logging import debug
from flask import Flask, render_template, url_for
import random

app = Flask(__name__)

@app.route("/")
def home():
    num=random.randint(1,6)
    return render_template("index.html", random_number = num)


if __name__ == "__main__":
    app.run(debug=True)
