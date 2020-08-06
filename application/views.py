from application import app
from .functions import getData, saveData, readData
from flask import request, render_template
from wtforms import Form, FormField, validators, TextField

class Search(Form):
    technology = TextField('Technology', validators = [validators.required()])
    location = TextField('Location')

@app.route('/')
def index():
    form = Search(request.form)
    return render_template('index.html', form = form)


