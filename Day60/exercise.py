# from flask import Flask, render_template, request
# app = Flask(__name__)
#
#
# @app.route('/')
# def home():
#     return render_template("exercise.html")
#
#
# @app.route("/login", methods=["POST"])
# def receive_data():
#     name = request.form["username"]
#     password = request.form["password"]
#     return f"<h1>Name: {name}, Password: {password}</h1>"
#
#
# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request
import requests
import smtplib


def send_email():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user="testepythoncesar@gmail.com", password="wehmogqtrsvhtpzh")
        connection.sendmail(
            from_addr="testepythoncesar@gmail.com",
            to_addrs="cesarsilveira35@gmail.com",
            msg="Subject: Contact request! \n\n"
                "Name:{nm}\n"
                "Email:{em}\n"
                "phone:{phn}\n"
                "Message:{msg}\n"
        )

send_email()

