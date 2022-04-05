import os
from flask import Flask
from flask_restful import Api
from database.db import initialize_db
from resources.routes import initialize_routes

app = Flask(__name__)
api = Api(app)

app.config['MONGO_SETTINGS'] = {
      'host' : os.environ['MONGODB_URI']
      # 'host' : 'mongodb+srv://mbdbarrios:Db4rr10smongo@cluster0.9sguj.mongodb.net/dbmusic?retryWrites=true&w=majority'
}

initialize_db(app)
initialize_routes(api)

app.debug = False
app.run()