from flask import Flask
from flask_restful import Api
from database.db import initialize_db
from resources.routes import initialize_routes

app = Flask(__name__)
api = Api(app)

app.config['MONGO_SETTINGS'] = {
    'host' : 'mongodb://localhost:27017'
}

initialize_db(app)
initialize_routes(api)

app.debug = True
app.run()