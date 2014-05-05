__author__ = 'nevelina'
from flask import render_template, flash, redirect
from app import app
from form import SimpleForm

@app.route('/', methods=['GET', 'POST'])
def home_page():
	return render_template('home_page.html', title='KnowFashion Home')

@app.route('/browse', methods=['GET', 'POST'])
def browse():
    return render_template('browse.html',
        title='Browse user uploaded things')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
	form = SimpleForm()
	return render_template('submit.html', title='Submit new artcile', form=form)

