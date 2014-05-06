__author__ = 'nevelina'
from flask import render_template, flash, redirect, request, url_for
from flask.ext.uploads import delete, init, save, Upload
import os
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
	if form.validate_on_submit():
		print 'lala'
		return redirect('/thankyou')        
	#if request.method == 'POST':
		#pic = request.files['upload']
		#print 'saving'
		#pic.save(os.path.join(app.config['UPLOADS_FOLDER'], 'wow.jpg'))
		#return 'Upload complete'
	else: 
		return render_template('submit.html', title='Submit new artcile', form=form)
	
@app.route('/thankyou', methods=['GET', 'POST'])
def thankyou():
	return render_template('thankyou.html', title='Thank you!')

