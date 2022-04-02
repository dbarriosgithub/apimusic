from .db import db

class Song(db.Document):
    track_code = db.StringField(required=True,unique=True)
    autor_name = db.StringField(required=True)
    title = db.StringField(required=True)
    album_name = db.StringField(required=True)
    song_year = db.IntField(required=True)
    duration = db.IntField(required=True)
