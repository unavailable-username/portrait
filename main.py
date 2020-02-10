from flask import Flask, render_template
from google.cloud import storage
from jinja2 import Template
import os
# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

BUCKET_NAME = "baker-portfolio"
IMAGE_FOLDER = '/static/images'

@app.route('/')
def index():
    """ Handle requests to the index(/) by returning a list of files in the image folder """

    response = '<head><script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script></head>'
    response += '<h1>Welcome to the Portfolio application.</h1>'
    response += '<div>A work in progress</div>'
    response += '<a href="https://bkr.family">Blog</a>'
    response += get_images_list_html(IMAGE_FOLDER)
    response += get_blob_names_html(BUCKET_NAME)
    response += get_images_js_html(BUCKET_NAME)
    return response

@app.route('/jinja.html')
def jinja_index():
    return render_template('index.html', example_string="Hello World", example_list=[0,1,2,3,4,5])

def get_images_list_html(image_folder:str) -> str:
    response = "<h4>From python app storage</h4>"
    response += "<ul>"
    for file in os.listdir(f'.{image_folder}'):
        response += f'<li><a href="{image_folder}/{file}">{file}</a></li>'
    response += "</ul>"
    return response

# Taken and modified from: https://cloud.google.com/storage/docs/listing-objects#rest-list-objects
def get_blob_names_html(bucket_name:str) -> str:
    """Lists all the blobs in the bucket."""
    storage_client = storage.Client()
    blobs = storage_client.list_blobs(bucket_name)
    response = "<h4>From google storage</h4>"
    response += "<ul>"
    for blob in blobs:
        response += f'<li><a href="https://{blob.bucket.name}.storage.googleapis.com/{blob.name}">{blob.name}</a></li>'
    response += "</ul>"
    return response

def get_images_js_html(bucket_name:str) -> str:
    return """
        <h4>From JSON REST API + JQ</h4>
        <script>
        f = fetch('https://storage.googleapis.com/storage/v1/b/baker-portfolio/o', {
        headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
        }
        }).then((response) => {
            return response.json();
        }).then((json) => {
            console.log(json);
            json.items.forEach(item => {
                $("#jq").append(`<li><a href="${item.mediaLink}">${item.name}</a></li>`);
            });
        });
        </script><ul id="jq"></ul>"""

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)