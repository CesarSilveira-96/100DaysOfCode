# Terminal command to work ---> python -m flask --app Day54.hello run <---

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def bye_world():
    return "<p>Goodbye, World!<p>"

if __name__ == "__main__":
    app.run()