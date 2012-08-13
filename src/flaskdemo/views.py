# Imports an object that was initialized in __init__.py. 
from flaskdemo import app
from flask import request, render_template

##
## Our pages
##

@app.route('/contacts/<areacode>')
def index(areacode='917'):
  contact = request.args.get('name', 'Adrianne')
  return render_template(
    'contacts.html',
    contacts = [
                 (contact, '({}) 555-9876'.format(areacode))
               ]
  )
