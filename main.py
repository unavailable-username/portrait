from flask import Flask
import os
# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
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

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)