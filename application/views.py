from application import app
from .functions import getData, saveData, readData
from wtforms import Form, FormField, validators, TextField

class Search(Form):
    technology = TextField('Technology', validators= validators)
    location = TextField('Location')


