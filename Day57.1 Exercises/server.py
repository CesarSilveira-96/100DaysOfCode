from flask import Flask, render_template
import requests
import random
import datetime

app = Flask(__name__)

@app.route("/")
def homepage():
    random_number = random.randint(1,10)
    current_year = datetime.datetime.now().year
    return render_template("index.html",rand_num=random_number, year=current_year)

@app.route("/guess/<username>")
def get_guess(username):
    name = username.capitalize()
    gender_response = requests.get(f"https://api.genderize.io?name={name}")
    gender_data = gender_response.json()["gender"]
    age_response = requests.get(f"https://api.agify.io?name={name}")
    age_data = age_response.json()["age"]

    return render_template("guess.html", name_to_guess=name, gender= gender_data, age= age_data)

@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/760b067c1132d0ed8d5c"
    response = requests.get(blog_url)
    all_posts = response.json()["blogs"]
    return render_template("blog.html", posts= all_posts)

if __name__ =="__main__":
    app.run(debug=True)


