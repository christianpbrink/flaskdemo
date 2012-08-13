# Imports an object that was initialized in __init__.py. 
from flaskdemo import app
from flask import request

##
## Our pages
##

@app.route('/contacts/<areacode>')
def index(areacode='917'):
  contact = request.args.get('name', 'Adrianne')
  return '{}: ({}) 555-9876'.format(contact, areacode)
