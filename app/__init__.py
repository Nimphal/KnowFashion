__author__ = 'nevelina'
from flask import Flask, redirect, request, url_for
from flask_wtf.csrf import CsrfProtect

app = Flask(__name__)
app.config.from_object('config')
CsrfProtect(app)

from app import views
