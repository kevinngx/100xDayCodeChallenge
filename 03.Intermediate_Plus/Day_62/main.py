from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    opening_time = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    closing_time = StringField('Closing Time e.g. 5:30pm', validators=[DataRequired()])
    rating = StringField('Coffee Rating', validators=[DataRequired()])
    wifi = StringField('Wifi Strength Rating', validators=[DataRequired()])
    power = StringField('Power Socket Availability', validators=[DataRequired()])
    submit = SubmitField('Submit')

    

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    
    form = CafeForm()    
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with if form.validate_on_submit()
    #TODO: Write validators


    if request.method == "POST":
        if form.validate_on_submit():
            print("SUCCESS")
            #TODO: Write data to CSV
            with open('cafe-data.csv', 'a', newline='') as csv_file:
                writer_object = csv.writer(csv_file)
                list = [form.cafe.data, form.location.data, form.opening_time.data, form.closing_time.data, form.rating.data, form.wifi.data, form.power.data]
                print(list)
                writer_object.writerow(list)
                print("Write Successful!")

            return render_template('add.html', form=form, success=True)
        
    return render_template('add.html', form=form, success=False)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)


