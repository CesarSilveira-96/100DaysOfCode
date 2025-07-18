from flask import Flask, render_template, request
import requests
import smtplib

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        send_email(name,email,phone,message)
        return render_template("contact.html", msg_sent=True)
    else:
        return render_template("contact.html")

# @app.route("/form-entry", methods=["POST"])
# def receive_data():
#     name = request.form["name"]
#     email = request.form["email"]
#     phone = request.form["phone"]
#     message = request.form["message"]
#     return f"<p>Name: {name}</p><p>Email: {email}</p><p>Phone: {phone}</p><p>Message: {message}</p>"
#
#
def send_email(nm,em,phn,msg):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user="testepythoncesar@gmail.com", password="wehmogqtrsvhtpzh")
        connection.sendmail(
            from_addr="testepythoncesar@gmail.com",
            to_addrs="cesarsilveira35@gmail.com",
            msg=f"Subject: Contact request! \n\n "
                f"Name: {nm}\n"
                f"Email: {em}\n"
                f"phone: {phn}\n"
                f"Message: {msg}\n"
        )

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
