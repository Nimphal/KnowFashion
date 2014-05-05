__author__ = 'nevelina'
from flask import render_template, flash, redirect
from app import app
from form import SimpleForm

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SimpleForm()
    return render_template('index.html',
        title='Form',
        form=form)
