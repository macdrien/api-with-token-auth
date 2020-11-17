from database.movie_db import MovieDB
from mappers.movie_mappers import MovieMappers

class MovieServices:
    def get_all():
        movies = MovieMappers.cursor_to_list(MovieDB.find_all())
        for movie in movies:
            movie['_id'] = MovieMappers.id_to_string(movie['_id'])
        return movies

    def get_by_id(index):
        movie = MovieDB.find_by_id(index)
        
        if movie is not None:
            movie['_id'] = MovieMappers.id_to_string(movie['_id'])

        return movie

    def create(movie):
        inserted_movie_id = MovieDB.insert(movie)
        return {'_id': str(inserted_movie_id)}

    def update(index, movie):
        return MovieDB.update(index, movie)

    def delete(index):
        return MovieDB.delete(index)