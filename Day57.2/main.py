from flask import Flask, render_template
import requests

blog_url = "https://api.npoint.io/760b067c1132d0ed8d5c"
response = requests.get(blog_url)
all_posts = response.json()["blogs"]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", posts=all_posts)

@app.route("/post/<int:num>")
def get_post(num):
    return render_template("post.html", posts= all_posts, number= num)

if __name__ == "__main__":
    app.run(debug=True)
