from flask import Flask, render_template, redirect, request, session, request, jsonify, url_for
from routes import ROUTES
import json


app = Flask(__name__)

@app.route("/")
def index():
  return render_template(ROUTES.HOME)

@app.route('/about')
def about():
  return 'The about page'