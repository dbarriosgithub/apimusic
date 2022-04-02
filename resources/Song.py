from importlib.resources import Resource
from flask import  Response,request
from database.models import Song
from flask_restful import Resource

# Enpoint class for get many items
class SongsApi(Resource):
    def get(self):
        songs = Song.objects().to_json()
        return Response(songs,mimetype="application/json",status=200)

    def post(self):
        body = request.get_json()
        song = Song(**body).save()
        id = song.id
        return {'id':str(id)},200


# Endpoint Class for get invidual item       
class SongApi(Resource):
    def get(self,id):
        song = Song.objects().get(id=id).to_json()
        return Response(song,mimetype="application/json",status=200)
    
    def put(self,id):
        body = request.get_json()
        Song.objects().get(id=id).update(**body)
        return '',200

    def delete(self,id):
        Song.objects().get(id=id).delete()
        return '',200
