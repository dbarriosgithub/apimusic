from flask_mongoengine import MongoEngine
import certifi

db = MongoEngine()

def initialize_db(app):
    db.connect(host="mongodb+srv://mbdbarrios:Db4rr10spc@cluster0.9sguj.mongodb.net/test?retryWrites=true&w=majority",tlsCAFile=certifi.where())
    #db.connect(host="mongodb://localhost:27017")
    #db.init_app(app)
