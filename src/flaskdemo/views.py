# Imports an object that was initialized in __init__.py. 
from flaskdemo import app
from flask import request, render_template, redirect
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

@app.route('/update', methods=['GET', 'POST'])
def update():
  if request.method == 'GET':
    return render_template('update.html')
  else:
    name   = request.form.get('name')
    number = request.form.get('number')
    print (name, number)
    if name:
      match = db_session.query(Contact).filter(Contact.name == name).first()
      if match:
        match.number = number
      else:
        c = Contact(name, number)
        db_session.add(c)
        db_session.commit()
    return redirect("/contacts")

