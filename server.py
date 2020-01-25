# Import everything we're going to use
from flask import Flask
import os
app = Flask(__name__)

IMAGE_FOLDER = '/static/images'

@app.route('/')
def index():
    """ Handle requests to the index(/) by returning a list of files in the image folder """
    response = "<ul>"
    for file in os.listdir(f'.{IMAGE_FOLDER}'):
        response += f'<li><a href="{IMAGE_FOLDER}/{file}">{file}</a></li>'
    response += "</ul>"
    return response