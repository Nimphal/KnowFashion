__author__ = 'nevelina'
from flask.ext.wtf import Form
from wtforms.fields import TextField

class SimpleForm(Form):
    brand = TextField('Brand name')
    clothing_type = TextField('Clothing type')
    colour = TextField('Colour')