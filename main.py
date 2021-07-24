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
        server.login("diener.stefan.daniel@gmail.com", os.environ.get('EMAIL_PW_DIENERSTEFANDANIEL'))
        server.sendmail("diener.stefan.daniel@gmail.com", "sdiener7@gmail.com", subject_message)
        server.quit()

    return render_template("index.html")

@app.route("/sent", methods=['POST'])
def sendmail():
    num = random.randint(1,6)
    return 



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
