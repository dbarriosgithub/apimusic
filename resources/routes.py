from .song import SongsApi,SongApi

def initialize_routes(api):
    # Plural routes for many items request
    # an singular routes for individual item request 
    api.add_resource(SongsApi, '/api/songs')
    api.add_resource(SongApi, '/api/song/<id>')


