# Import everything we're going to use
from flask import Flask
import os
app = Flask(__name__)

# Add the route for the index
@app.route('/')
def index():
    # Start the unordered list
    response = "<ul><li>"
    # retrieve all of the files and add them to the list
    response += "</li><li>".join(os.listdir("./static/images"))
    # end the list
    response += "</li></ul>"
    return response