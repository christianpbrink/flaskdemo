# Imports an object that was initialized in __init__.py. 
from flaskdemo import app


##
## Our pages
##

@app.route('/contacts')
def index():
  return 'Adrianne: (917) 555-9876'
