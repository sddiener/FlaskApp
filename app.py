from logging import debug
from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():
    return "<p> This was printed by FLAAASK! :D</p>"

if __name__ == "__main__":
    app.run(debug=True)
