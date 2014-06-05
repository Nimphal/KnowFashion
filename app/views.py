__author__ = 'nevelina'
from flask import render_template, flash, redirect, request, url_for
from flask import Flask, Response, request, abort, render_template_string, send_from_directory
from PIL import Image
import StringIO
from werkzeug.utils import secure_filename
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

@app.route('/<path:filename>')
def image(filename):
    try:
        w = int(request.args['w'])
        h = int(request.args['h'])
    except (KeyError, ValueError):
        return send_from_directory('.', filename)

    try:
        im = Image.open(filename)
        im.thumbnail((w, h), Image.ANTIALIAS)
        io = StringIO.StringIO()
        im.save(io, format='JPEG')
        return Response(io.getvalue(), mimetype='image/jpeg')

    except IOError:
        abort(404)

    return send_from_directory('.', filename)

WIDTH = 1000
HEIGHT = 800

@app.route('/browse', methods=['GET', 'POST'])
def browse():
    images = []
    for root, dirs, files in os.walk('.'):
        for filename in [os.path.join(root, name) for name in files]:
            if not filename.endswith('.jpg'):
                continue
            im = Image.open(filename)
            w, h = im.size
            aspect = 1.0*w/h
            if aspect > 1.0*WIDTH/HEIGHT:
                width = min(w, WIDTH)
                height = width/aspect
            else:
                height = min(h, HEIGHT)
                width = height*aspect
            images.append({
                'width': int(width),
                'height': int(height),
                'src': filename
            })
    return render_template('browse.html',
                           title='Browse user uploaded things', **{'images': images})


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = SimpleForm(request.form)

    if request.method == 'POST':  # and form.validate(): -- this doesn't validate, for whatever reason

        filename = ""
        pic = request.files['upload']

        if not pic:
            print 'not pic'
        if pic and allowed_file(pic.filename):
            filename = secure_filename(pic.filename)
            pic.save(os.path.join(app.config['UPLOADS_FOLDER'], filename))

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

    return render_template('submit.html', title='Submit new artcile', form=form)


@app.route('/thankyou', methods=['GET', 'POST'])
def thankyou():
    return render_template('thankyou.html', title='Thank you!')

