__author__ = 'nevelina'
from flask import render_template, flash, redirect, request, url_for
from flask.ext.uploads import delete, init, save, Upload
import os
from app import app
from form import SimpleForm
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()


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
	if request.method == 'POST': #and form.validate(): -- this doesn't validate, for whatever reason
		pic = request.files['upload']
		print 'saving'
		pic.save(os.path.join(app.config['UPLOADS_FOLDER'], form.brand.data + '_' + form.clothing_type.data + '_' + form.colour.data))
		doc = {
			'title': form.colour.data + ' ' + form.clothing_type.data + ' ' + 'from ' + form.brand.data,
			'brand': form.brand.data,
			'store': form.store.data,
			'clothing_type': form.clothing_type.data,
			'colour': form.colour.data,
			'country': form.country.data,
			'price': form.price.data,
			'currency': form.currency.data,
			'date_of_purchase': form.date_purchased.data,
			'pic_title': form.brand.data + '_' + form.clothing_type.data + '_' + form.colour.data
			}
		doc_id = form.brand.data + '_' + form.clothing_type.data + '_' + form.colour.data + '_' + '1'
		
		res = es.index(index="garments", doc_type='item', id=doc_id, body=doc)
		return redirect(url_for('thankyou'))        
	#if request.method == 'POST':
		#pic = request.files['upload']
		#print 'saving'
		#pic.save(os.path.join(app.config['UPLOADS_FOLDER'], 'wow.jpg'))
		#return 'Upload complete'
	#else: 
	return render_template('submit.html', title='Submit new artcile', form=form)
	
@app.route('/thankyou', methods=['GET', 'POST'])
def thankyou():
	return render_template('thankyou.html', title='Thank you!')

