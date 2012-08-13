# Imports an object that was initialized in __init__.py. 
from flaskdemo import app
from flask import request, render_template
from database import init_db, db_session
from models import *

init_db()

##
## Our pages
##

@app.route('/contacts/', defaults={'name' : None})
@app.route('/contacts/<name>')
def contacts(name=None):
  if name:
    cs = db_session.query(Contact).filter(Contact.name.contains(name))
  else:
    cs = db_session.query(Contact).all()
  return render_template(
    'contacts.html',
    contacts = [(c.name, c.number) for c in cs])
