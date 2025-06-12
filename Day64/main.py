from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap5 import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.fields.simple import URLField
from wtforms.validators import DataRequired

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# CREATE DB
class Base(DeclarativeBase):
  pass

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-ranking.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer,nullable=False)
    review: Mapped[str] = mapped_column(String(80), nullable=False)
    synopsis: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    img_url: Mapped[str] = mapped_column(String, nullable=False)

with app.app_context():
    db.create_all()

class MovieForm(FlaskForm):
    movie_title = StringField("Movie title:", validators=[DataRequired()])
    year = IntegerField("Year of release")
    movie_synopsis = StringField("Movie synopsis:", validators=[DataRequired()])
    review = StringField("Your review of this movie:", validators=[DataRequired()])
    movie_rating = FloatField("Movie rating (out of 10):", validators=[DataRequired()])
    img_url = URLField("Image URL:", validators=[DataRequired()])
    submit = SubmitField("Add")

@app.route("/")
def home():
    order = db.select(Movie).order_by(Movie.rating.desc())
    movies = db.session.execute(order).scalars().all()[:10]
    return render_template("index.html",list=movies, lenght=len(movies))

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        #UPDATE RECORD
        movie_id = request.form["id"]
        movie_to_update = db.get_or_404(Movie, movie_id)
        movie_to_update.rating = float(request.form["rating"])
        movie_to_update.review = request.form["review"]
        db.session.commit()
        return redirect(url_for('home'))
    movie_id = request.args.get('id')
    movie_selected = db.get_or_404(Movie, movie_id)
    return render_template("edit.html", movie=movie_selected)

@app.route("/add", methods=["GET", "POST"])
def add():
    form = MovieForm()
    if form.validate_on_submit():
        new_movie_dict = {
        "title":form.movie_title.data,
        "year":form.year.data,
        "review":form.review.data,
        "synopsis":form.movie_synopsis.data,
        "rating":form.movie_rating.data,
        "img_url":form.img_url.data
        }
        existing_movie = db.session.execute(db.select(Movie).filter_by(title=form.movie_title.data)).scalar()
        if existing_movie:
            # Exibir uma mensagem de erro ou redirecionar
            return "Filme já existe!", 400
        new_movie = Movie(
            title=form.movie_title.data.title(),
            year=form.year.data,
            review=form.review.data.capitalize(),
            synopsis=form.movie_synopsis.data.title(),
            rating=form.movie_rating.data,
            img_url=form.img_url.data
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html", form=form)

@app.route("/delete")
def delete():
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)
