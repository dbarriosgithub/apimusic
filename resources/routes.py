from .Song import SongsApi,SongApi
from .user import UserApi

def initialize_routes(api):
    # Plural routes for many items request
    # and singular routes for individual item request 
    api.add_resource(SongsApi, '/api/songs')
    api.add_resource(SongApi, '/api/song/<id>')
    api.add_resource(UserApi, '/api/user')




