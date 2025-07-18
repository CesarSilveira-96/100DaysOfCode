from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, URLField
from wtforms.validators import DataRequired
import pandas
import csv

'''
On Windows type:
python -m pip install -r requirements.txt
'''

hours = [f"{hour}:00" for hour in range(0, 24)]

cafes_data = pandas.read_csv('cafe-data.csv')

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField('Location URL', validators=[DataRequired()])
    coffee = SelectField('Coffee rating', validators=[DataRequired()],
                         choices=["✘", "☕", " ☕ ☕", " ☕ ☕ ☕", " ☕ ☕ ☕ ☕", " ☕ ☕ ☕ ☕ ☕"])
    opens = SelectField('Open time', validators=[DataRequired()], choices=hours)
    closes = SelectField('Closing time', validators=[DataRequired()], choices=hours)
    wifi = SelectField('Wifi speed', validators=[DataRequired()], choices=["✘", "🛜", "🛜🛜", "🛜🛜🛜", "🛜🛜🛜🛜", "🛜🛜🛜🛜🛜"])
    power = SelectField("Power outlet", validators=[DataRequired()],
                        choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"])
    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET","POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open ('cafe-data.csv', mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.opens.data},"
                           f"{form.closes.data},"
                           f"{form.coffee.data},"
                           f"{form.wifi.data},"
                           f"{form.power.data}")
            return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)

