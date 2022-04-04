# Apimusic
A little implementation of flaskapi rest with mongoDb and Python flask.

## Getting Started
Please follow these simple steps.

### Prerequisites
Make sure you have Python Install on your machine, and also install MongoDB.
### Instalation
The API service for Music Play List to manage of songs. From your console, run the following:<br>
→mkdir music-api<br>
→cd music-api<br>

Then install Pipenv:
→pip install --user pipenv<br>

After this, we will then install Flask.<br>
→Pipenv install flask.<br>
This will create a virtual environment and install Flask. It will generate two files for us, Pipfile and Pipfile.lock.

To activate the virtual environment created by Pipenv, run pipenv shell:
→ pipenv shell

To install Flask-Restful, run:
→ pipenv install flask-restful

To install MongoEngine:
→ pipenv install flask-mongoengine

### Otherwise
You can clone the enterily project in your local system,active Pipenv and run app.py file.<br><br>
Test the next endpoints using postman or another tools:<br>
→ http://yourdomain.com/api/songs<br>
`Method POST -> add new song`<br>
`Method GET  -> get all songs`<br>
→ http://yourdomain.com/api/song/id<br>
`Ej http://yourdomain.com/api/song/7c654443bc`<br><br>
→ http://yourdomain.com/api/user<br>
`Method POST -> create new user system`<br>
`Method GET  -> Autenticate user and get bearer token`




