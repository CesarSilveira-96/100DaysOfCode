from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap5 import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

'''

On Windows type:
python -m pip install -r requirements.txt

'''

class Base(DeclarativeBase):
  pass

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///book-library.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATING TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # # allows each book object to be identified by its title when printed.
    # def __repr__(self):
    #     return f'<Book {self.title}>'

with app.app_context():
    db.create_all()

class BookForm(FlaskForm):
    book_title = StringField("Book Title:", validators=[DataRequired()])
    book_author = StringField("Book Author:", validators=[DataRequired()])
    book_rating = FloatField("Book rating (1 to 10):", validators=[DataRequired()], default=1.0)
    submit = SubmitField("Add")

Bootstrap(app)

all_books = []

@app.route('/')
def home():
    books = db.session.execute(db.select(Book)).scalars().all()
    return render_template("index.html", list=books, lenght=len(books))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = BookForm()
    if form.validate_on_submit():
        new_book_dict = {
        "title":form.book_title.data,
        "author":form.book_author.data,
        "rating":form.book_rating.data
        }
        if new_book_dict not in all_books:
            all_books.append(new_book_dict)
        #
        # print(all_books)
        existing_book = db.session.execute(db.select(Book).filter_by(title=form.book_title.data)).scalar()
        if existing_book:
            # Exibir uma mensagem de erro ou redirecionar
            return "Livro já existe!", 400
        new_book = Book(
            title=form.book_title.data.title(),
            author=form.book_author.data.title(),
            rating=form.book_rating.data
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html", form=form)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        #UPDATE RECORD
        book_id = request.form["id"]
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = float(request.form["rating"])
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = db.get_or_404(Book, book_id)
    return render_template("edit_rating.html", book=book_selected)

@app.route("/delete", methods=["GET", "POST"])
def delete():
    book_id = request.args.get('id')
    # DELETE RECORD
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

