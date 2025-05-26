# Terminal command to work ---> python -m flask --app Day54.hello run <---
import random

from flask import Flask

app = Flask(__name__)
rand_number = random.randint(0,10)
print(rand_number)

# Creating decorators for text styling
def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

# >>>>>>>>>>>>>> GUESS SITE PROJECT <<<<<<<<<<<<<<<
# @app.route("/")
# @make_bold
# def hello_world():
#     return "<p>Hello, World!</p>"
#
# @app.route("/bye")
# def bye_world():
#     return "<p>Goodbye, World!</p>"
#
# @app.route("/username/<name>")
# def greet(name):
#     return f"<p>Hello, {name}!</p>"

@app.route("/")
@make_bold
def guess_home():
    return ("<h1 style='text-align: center'> Guess a number between 0 and 10 by adding /number to the url above! </h1>"
            "<img src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaWdib3hjdDVyMDNsbThweHQ0d3h0MjUxb2dtamxmMmMzbX"
            "lodXE0ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/iibEPf8xEDTedJcDJr/giphy.gif' "
            "style='display: block; margin: auto'/>")

@app.route("/<int:number>")
def guess_number(number):
    try:
        if number == rand_number:
            return ("<h1 style='text-align: center; color: green'>You've got it right!</h1>"
                    f"<h2 style='text-align: center; color: green'>The number was {number}</h2>"
                    "<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjJkc2I5Yzh2Y2RmYTRyemNnZjZ0NGoxcmh2c"
                    "jh1Mm01a3B3bWdtaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/tIeCLkB8geYtW/giphy.gif' "
                    "style='display: block; margin: auto'>")
        elif number > rand_number:
            return ("<h1 style='text-align: center; color: blue'>Too high, try again!</h1>"
                    "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWVxNjNhejFuZHg4cWp4anptcWM5ajRxY3FnMX"
                    "ZxOWQwbWFuYXAybyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/2cei8MJiL2OWga5XoC/giphy.gif' "
                    "style='display: block; margin: auto'/>")
        elif number < rand_number:
            return ("<h1 style='text-align: center; color: red'>Too low, try again!</h1>"
                    "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbzR0eHB3ZDgzZHU2bDhoMm9hdDIyMWptZnJjc2"
                    "9ybXJzdTEzN2pmNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Mq1MUGwNKcTxFePEZo/giphy.gif' "
                    "style='display: block; margin: auto'/>")
        else:
            return None
    except ValueError:
        return f"<p>Numbers only, try again!</p>"

if __name__ == "__main__":
    app.run(debug=True)