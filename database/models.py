from .db import db

class Song(db.Document):
    track_code = db.StringField(required=True,unique=True)
    autor_name = db.StringField(required=True)
    title = db.StringField(required=True)
    album_name = db.StringField(required=True)
    song_year = db.IntField(required=True)
    duration = db.IntField(required=True)
    playlist_owner = db.StringField(required=True)

class User(db.Document):
    email = db.StringField(required=True,unique=True)
    password = db.StringField(required=True)
    start_time = db.StringField(required=True,unique=True)
    login_state = db.IntField(required=True)
    token = db.StringField(required=True)
