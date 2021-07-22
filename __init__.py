from logging import debug
from flask import Flask, render_template, url_for, request
import random
import smtplib
import os

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")

        subject_message = 'Subject: {}\n\n{}'.format(subject, message)

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("diener.stefan.daniel@gmail.com", os.environ.get('EMAIL_PW_DIENERSTEFANDANIEL')) #TODO: set environment varialbe for PW!!!!!!
        server.sendmail("diener.stefan.daniel@gmail.com", "sdiener7@gmail.com", subject_message)
        server.quit()

    return render_template("index.html")

@app.route("/projects", methods=['POST', 'GET'])
def projects():
    num = random.randint(1,6)
    return render_template("projects.html", random_number = num)



if __name__ == "__main__":
    app.run(debug=True)
    app.run(host = "0.0.0.0", port = 5000)
