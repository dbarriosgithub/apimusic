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
Api use **Bearer token for authentication**<br><br>

→ http://yourdomain.com/api/user<br>
`Method POST -> create new user system`<br>
`Method GET  -> Authenticate user and get Bearer token`<br><br>

→ http://yourdomain.com/api/songs<br>
`Method GET  -> get all songs`<br>
`Method POST -> add a new song`<br><br>
EJ BODY<br>
{
    "track_code" : "t1",
    "autor_name" : "Adele",
    "title" : "Someone like you",
    "album_name" : "21",
    "song_year" : 2020,
    "duration" : 30
}<br>

→ http://yourdomain.com/api/song/id<br>
`Method PUT -> Update song element by ID`<br>
`Method GET  -> Get song element by ID`<br>
`Method DELETE  -> Delete song element by ID`<br>

`Ej http://yourdomain.com/api/song/7c654443bc`<br><br>

### Heroku demo
You can test the api using the next endpoints:<br>

→ https://music-api-00.herokuapp.com/api/user<br>
`Method POST -> create new user system`<br>
`Method GET  -> Authenticate user and get` **Bearer token**<br><br>

→ https://music-api-00.herokuapp.com/api/songs<br>
`Method GET  -> get all songs`<br>
`Method POST -> add a new song`<br><br>
**body structure**<br>
{
    "track_code" : "t1",
    "autor_name" : "Adele",
    "title" : "Someone like you",
    "album_name" : "21",
    "song_year" : 2020,
    "duration" : 30
}<br>
**note:** track_code unique key<br><br>

→ https://music-api-00.herokuapp.com/api/song/id<br>
`Method PUT -> Update song element by ID`<br>
`Method GET  -> Get song element by ID`<br>
`Method DELETE  -> Delete song element by ID`<br>

Ej `https://music-api-00.herokuapp.com/api/song/624c9e0d82c2fbc8673036c0`<br><br>
**note:** oid = id <br>
 "_id": {
        "$oid": "624c9e0d82c2fbc8673036c0"
    },







