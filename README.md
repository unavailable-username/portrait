# Portrait

A flask app for serving images and a description in the browser.

### Technologies Used
* Python 3.7
* Windows or Linux
* Flask 1.1.x

## Setup + Running (Linux)
Create a virtual env
```
python3 -m venv venv
. venv/bin/activate
pip install Flask
```

Run the application
```
export FLASK_APP=main.py
flask run
```

## Setup + Running (Windows)
Create a virtual env
```
py -3 -m venv venv
venv\Scripts\activate
pip install Flask
```

Run the application
```
set FLASK_APP=main.py
flask run
```

# Update requirements.txt
While in virtual env: `pip freeze > requirements.txt`

# Setup credentials
https://cloud.google.com/docs/authentication/getting-started
`export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/[FILE_NAME].json"`

# Deploying to GCP

To deploy to a GCP app engine
```
gcloud app deploy
gcloud app browse
```