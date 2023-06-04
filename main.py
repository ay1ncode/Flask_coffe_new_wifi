from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import csv
from myform import Coffee_form

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'#you can create you own random key as well
Bootstrap(app)


# ---------------------------------------------------------------------------

# Route for the home page
@app.route("/")
def home():
    return render_template("index.html")


# Route for adding a new cafe
@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = Coffee_form()

    # Check if the form has been submitted
    if form.validate_on_submit():
        print("True")
        cafe = form.cafe.data
        coffee_loc = form.coffee_loc.data
        open_time = form.open_time.data
        close_time = form.close_time.data
        coffe_rate = form.coffee_rate.data
        wifi = form.wifi.data
        power_soc = form.power_soc.data

        # Open the CSV file and write the form data
        with open("cafe-data.csv", mode='a', newline='', encoding='utf-8') as file:
            csv_data = csv.writer(file, delimiter=',')
            row = [cafe, coffee_loc, open_time, close_time, coffe_rate, wifi, power_soc]  # Create a list from the form
            csv_data.writerow(row)  # Write a new row into the CSV

        return redirect(url_for('cafes'))  # Redirect after form submission

    return render_template('add.html', form=form)


# Route for displaying all cafes
@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')  # Read the CSV file
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        new_len = len(list_of_rows)  # Length of the list

    return render_template('cafes.html', cafes=list_of_rows, len_num=new_len)


if __name__ == '__main__':
    app.run(debug=True)
