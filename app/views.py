__author__ = 'nevelina'
from flask import render_template, flash, redirect, request, url_for
from flask import Flask, Response, request, abort, render_template_string, send_from_directory
from PIL import Image
from werkzeug.utils import secure_filename
import os
from app import app
from form import SimpleForm, BrowseForm
import requests
import json

from elasticsearch import Elasticsearch

es = Elasticsearch(hosts=[{'host': 'localhost', 'port': 9201}])


@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('home_page.html', title='KnowFashion Home')


@app.route('/browse', methods=['GET', 'POST'])
def browse():
    form = BrowseForm(request.form)
    return render_template('browse.html',
                           title='Browse user uploaded things', form=form)

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html',
                           title='About KnowFashion')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html',
                           title='Contact')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = SimpleForm(request.form)

    if request.method == 'POST' and form.validate(): #-- this doesn't validate, for whatever reason
        filename = ""
        if form.upload_url.data:
            filename = form.clothing_type.data + '_' + form.country.data + '_' + form.brand.data + '_' + form.colour.data
            f = open(os.path.join(app.config['UPLOADS_FOLDER'], filename), 'wb')
            f.write(requests.get(form.upload_url.data).content)
            f.close()
        elif request.files['upload']:
            pic = request.files['upload']
            if not pic:
                print 'not pic'
            if pic and allowed_file(pic.filename):
                filename = secure_filename(pic.filename)
                pic.save(os.path.join(app.config['UPLOADS_FOLDER'], filename))
                img = app.config['UPLOADS_FOLDER'] + '/' + filename
                im1 = Image.open(img)
                width = 250
                height = 350
                im5 = im1.resize((width, height), Image.ANTIALIAS)
                im5.save(os.path.join(app.config['UPLOADS_FOLDER'], filename))

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
            'pic_title': filename
        }
        doc_id = form.brand.data + '_' + form.clothing_type.data + '_' + form.colour.data

        res = es.index(index="garments", doc_type='item', id=doc_id, body=doc)
        return redirect(url_for('thankyou'))
    print json.dumps(form.errors, indent=3)

    return render_template('submit.html', title='Submit new artcile', form=form)


@app.route('/thankyou', methods=['GET', 'POST'])
def thankyou():
    return render_template('thankyou.html', title='Thank you!')
