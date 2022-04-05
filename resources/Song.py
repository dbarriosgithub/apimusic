from flask import  Response,request
from database.models import Song
from resources.user import UserApi
from flask_restful import Resource
from bson import ObjectId


# Meaning status code
# ----------------------
# Status-code	Meaning
#  200	        The request has succeeded.
#  201	        Request succeeded; a new resource has been created.
#  400	        Bad request; the server won’t process it due to a client error.
#  404	        Resource not found.

#Api Rules
# ------------------
#Users should be able to create a new element that can only be retrieved by themselves (Private item), or that can be retrieved by others (Public item).
#Users should be able to read all public elements in the table/collection.
#Users should be able to read all elements created by themselves.
#Users should be able to edit at least one field in one of their private items.
#Validate that users are trying to read or update their own private elements, otherwise send a meaningful response.


# Enpoint class for get MANY items
class SongsApi(Resource):
    # ---- get all Songs ----
    def get(self):
        bearer_token = getBearerToken()
        user = UserApi()
        resp = user.isValidToken(token=bearer_token)
        
        if resp[0]["response"] == True:
            songs = Song.objects().to_json()
            return Response(songs,mimetype="application/json",status=200)
        else:
            return resp

    #--- add song ---
    def post(self):
        body = request.get_json()
        # retrieve bearer token for validation
        bearer_token = getBearerToken()
        user = UserApi()
        resp = user.isValidToken(token=bearer_token)
        
        if resp[0]["response"] == True: #is valid token
            body["playlist_owner"] = resp[0]["user"]
            song = Song(**body).save()
            id = song.id
            return {'id':str(id)},200
        else:
            return resp



# ----------------------------------------
# Endpoint Class for get INDIVIDUAL item       
class SongApi(Resource):
    def get(self,id):

        bearer_token = getBearerToken()
        user = UserApi()
        resp = user.isValidToken(token=bearer_token)

        if resp[0]["response"] == True: #verify valid token
            
            try:
                if isValidObjId(id):
                    song = Song.objects().get(id=id)
                else:
                    return {"msg":" is not a valid ObjectId url"},404

            except Song.DoesNotExist:
                return {'msg' : 'Song does not exist'},404


            if song.playlist_owner == resp[0]["user"]: #valid item ownership
                return Response(song.to_json(),mimetype="application/json",status=200)
            else:
                return {"msg":"Access denied to this private item"},404
        else:
            return resp


    #  put class method
    # ----------------------------       
    def put(self,id):
        body = request.get_json()

        bearer_token = getBearerToken()
        user = UserApi()
        resp = user.isValidToken(token=bearer_token)

        if resp[0]["response"] == True: #verify valid token

            try:
                if isValidObjId(id):
                    song = Song.objects().get(id=id)
                else:
                    return {"msg":" is not a valid ObjectId url"},404

            except Song.DoesNotExist:
                return {'msg' : 'Song does not exist'},404

            if song.playlist_owner == resp[0]["user"]: #valid item ownership
                song.update(**body)
                return {"msg":"record update succesful"},200
            else:
                return {"msg":"Access denied to this private item"},404
        else:
            return resp

        
#    delete class method
#  ------------------------------------------
    def delete(self,id):

        bearer_token = getBearerToken()
        user = UserApi()
        resp = user.isValidToken(token=bearer_token)

        if resp[0]["response"] == True: #verify valid token

            try:
                if isValidObjId(id):
                    song = Song.objects().get(id=id)
                else:
                    return {"msg":" is not a valid ObjectId url"},404

            except Song.DoesNotExist:
                return {'msg' : 'Song does not exist'},404

            if song.playlist_owner == resp[0]["user"]: #valid item ownership
                song.delete()
                return {"msg":"record delete succesful"},200
            else:
                return {"msg":"Access denied to this private item"},404

        else:
            return resp
        


# --- Get Request bearer Token ----
def getBearerToken():
    headers = request.headers
    bearer = headers.get('Authorization') # Bearer YourTokenHere

    if bearer:
        token = bearer.split()[1]
        return token
    else:
        return ''

#------ verify correct string url --------
def isValidObjId(id):
    if ObjectId.is_valid(id):
        return True
    else:
        return False
