from flask import Flask, render_template
import requests



app = Flask(__name__)

@app.route("/")
def home():
    response = requests.get("https://api.npoint.io/65de24598fe6779c3552")
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route("/about")
def get_about():
    return render_template("about.html")

@app.route("/contact")
def get_contact():
    return render_template("contact.html")

@app.route("/sposts")
def get_sposts():
    return render_template("sposts.html")

@app.route("/post/<int:num>")
def get_post(num):
    response = requests.get("https://api.npoint.io/65de24598fe6779c3552")
    all_posts = response.json()
    return render_template(f"post.html", number= num, posts= all_posts)


if __name__ == "__main__":
    app.run(debug=True)
