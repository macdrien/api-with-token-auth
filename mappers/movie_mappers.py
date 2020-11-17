import json

class MovieMappers:
    def json_to_dict(movie):
        movie_dict = json.loads({
            '_id': movie['_id'],
            'name': movie['name'],
            'casts': movie['casts'],
            'genres': movie['genres']
        })
        return movie_dict
    
    def id_to_string(index):
        return str(index)
    
    def cursor_to_list(movies):
        result = []
        for movie in movies:
            result.append(movie)
        return result