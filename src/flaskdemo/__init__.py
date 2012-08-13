from flask import Flask

# this initializes the actual application object
app = Flask(__name__)

import flaskdemo.views
