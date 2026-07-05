from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    open = StringField('Open', validators=[DataRequired()])
    close = StringField('Close', validators=[DataRequired()])
    coffee = StringField('Coffee', validators=[DataRequired()])
    wifi = StringField('Wifi', validators=[DataRequired()])
    power = StringField('Power', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([
                form.cafe.data,
                form.location.data,
                form.open.data,
                form.close.data,
                form.coffee.data,
                form.wifi.data,
                form.power.data
            ])
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
