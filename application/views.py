from flask import request, render_template
from application import app
from wtforms import Form, validators, TextField
from .functions import save_data, read_data


class Search(Form):
    technology = TextField('Technology: ', validators=[validators.required()])
    location = TextField('Location: ')


@app.route('/')
def index():
    form = Search(request.form)
    return render_template('index.html', form=form)


@app.route('/job_offers', methods=('GET', 'POST'))
def search_job():
    if request.method == 'POST':
        description = request.form['technology']
        location = request.form['location']
        save_data(description, location)

    all_offers = read_data()

    return render_template('job_offers.html', description=description, location=location, job=all_offers)


