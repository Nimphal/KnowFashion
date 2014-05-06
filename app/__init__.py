__author__ = 'nevelina'
from flask import Flask, redirect, request, url_for
import flask.ext.uploads

app = Flask(__name__)
app.config.from_object('config')

from app import views
