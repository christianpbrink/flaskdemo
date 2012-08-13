from flask import Response, jsonify, request 
import json, os, sys
from pprint import pprint

# Imports an object that was initialized in __init__.py. 
from flaskdemo import app


##
## Our pages
##

@app.route('/')
def index():
  return render_template('index.html',
                      enumerate = enumerate,
                      str       = str,
                      zip       = zip)
