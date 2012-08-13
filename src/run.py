import sys
from flaskdemo import app

# We set our debug option using a command line argument.
debug = True if len(sys.argv) > 1 and sys.argv[1] == "debug" else False
app.run(debug=debug)
