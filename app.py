from flask import Flask
from flask_restful import Api
from database.db import initialize_db
from resources.routes import initialize_routes

app = Flask(__name__)
api = Api(app)

app.config['MONGO_SETTINGS'] = {
       'db': 'test',
       'host' : 'mongodb://localhost:27017'
       # 'host' : 'mongodb://mbdbarrios:Db4rr10spc@cluster0.9sguj.mongodb.net:27017/test'
}


initialize_db(app)
initialize_routes(api)

app.debug = True
app.run()