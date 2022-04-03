from flask import  Response,request
from database.models import User
from flask_restful import Resource
from datetime import datetime
import re


# Meaning status code
# ----------------------
# Status-code	Meaning
#  200	        The request has succeeded.
#  201	        Request succeeded; a new resource has been created.
#  400	        Bad request; the server won’t process it due to a client error.
#  404	        Resource not found.


class UserApi(Resource):

    # -------- start login autenticate method ------------------------
    
    def get(self):

        body = request.get_json()

        # get timestamp
        datetimeObj = datetime.now()
        string_timestamp = str(datetime.timestamp(datetimeObj))

        if self.isValid(string=body["email"],type="email") == False:    # verify valid email
            return {'msg' : 'Email is invalid'} 
        elif self.isValid(string=body["password"],type="pass") == False:     # verify password
            return {'msg': 'pass should be contains:contains at least 10 characters, one lowercase letter, one uppercase letter and one of the following characters: !, @, #, ? or ].'}

        #  verify if user exist
        try:
            user = User.objects().get(email=body["email"])
            if user is not None:
                try:
                    userObj = User.objects().get(email=body["email"],password=body["password"])

                    body["start_time"] = string_timestamp
                    body["token"] = "tk" + string_timestamp
                    body["login_state"] = 1

                    userObj.update(**body)
                    return {"token":body["token"]},200

                except User.DoesNotExist:
                    return {'msg':'user or password wrong'},400

        except User.DoesNotExist:
            return {'msg' : 'user does not exist'},404
    
    #  --------- start new user  method----------------------   
    #  ---------------------------------------------------------
    def post(self):

        body = request.get_json()

        if self.isValid(string=body["email"],type="email") == False:    #verify valid email
            return {'msg' : 'Email is invalid'} 
        elif self.isValid(string=body["password"],type="pass") == False:     # verify password
            return {'msg': 'pass should be contains:contains at least 10 characters, one lowercase letter, one uppercase letter and one of the following characters: !, @, #, ? or ].'}
            
        try:
            user = User.objects().get(email=body["email"])
            if user is not None:
                return {'msg':'User already exist'},400
        except User.DoesNotExist:
            # if user does not exist then save this
           
            body["start_time"] = ""
            body["token"] = ""
            body["login_state"] = 0

            user = User(**body).save()
            id = user.id
            return {'id':str(id)},201


    #-----method for validate actual TOKEN ------------
    def isValidToken(self,**kwargs):
        dt_obj_now = datetime.now()
        time_stamp_now = datetime.timestamp(dt_obj_now)

        try:
            user = User.objects().get(token = kwargs["token"])

            dt_object = datetime.fromtimestamp(float(user.start_time))
            dt_object_now  = datetime.fromtimestamp(time_stamp_now)

            dt_totalmin = (dt_object.hour * 60) + dt_object.minute
            total_min_now = (dt_object_now.hour *60) + dt_object_now.minute

            diference_min = total_min_now - dt_totalmin

            if(diference_min > 20): #token expire in 20 minutes
                return {'msg' : 'token expired','response' : False},404
            else:
                return {'msg' : 'token valid','response' : True,'user':user.email},201

                
        except User.DoesNotExist:
            return {'msg' : 'token unvalid','response' : False},404


    #------ method for validate email and password----
    def isValid(self,**kwargs):

        if(kwargs["type"] == "email"):
            regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        else:
            regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#?\]])[A-Za-z\d!@#?\]]{10,}$')

        
        if re.fullmatch(regex, kwargs["string"]):
            return True
        else:
            return False
