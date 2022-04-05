from flask import Flask
from flask_restful import Api
from database.db import initialize_db
from resources.routes import initialize_routes

app = Flask(__name__)
api = Api(app)

# app.config['MONGO_SETTINGS'] = {
#        'db': 'test',
#        'host' : 'mongodb://localhost:27017'
#        # 'host' : 'mongodb+srv://mbdbarrios:Db4rr10spc@cluster0.9sguj.mongodb.net/test?retryWrites=true&w=majority'
# }

initialize_db(app)
initialize_routes(api)

app.run(debug=True, port=33507)
app.run()