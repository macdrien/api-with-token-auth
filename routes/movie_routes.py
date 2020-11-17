from flask import Blueprint, request, Response, jsonify
from flask_jwt_extended import jwt_required

from common.http_status_code import HTTPStatusCode
from services.movie_services import MovieServices

movies = Blueprint('movies', __name__)

@movies.route('/movies', methods=['GET'])
@jwt_required
def get_movies():
    return jsonify(MovieServices.get_all()), HTTPStatusCode.OK.value

@movies.route('/movies/<index>', methods=['GET'])
def get_movie_by_id(index):
    movie = MovieServices.get_by_id(index)
    
    if movie is not None:
        return jsonify(movie), HTTPStatusCode.OK.value
    else:
        return '', HTTPStatusCode.NOT_FOUND.value

@movies.route('/movies', methods=['POST'])
def create_movie():
    body = request.get_json()
    return jsonify(MovieServices.create(body)), HTTPStatusCode.CREATED.value

@movies.route('/movies/<index>', methods=['PUT'])
def update_movie(index):
    body = request.get_json()
    modified_count = MovieServices.update(index, body)

    if modified_count == 1:
        return jsonify(body), HTTPStatusCode.OK.value
    else:
        return jsonify({'modified_count': modified_count}), HTTPStatusCode.BAD_REQUEST.value

@movies.route('/movies/<index>', methods=['DELETE'])
def delete_movie(index):
    if MovieServices.delete(index):
        return '', HTTPStatusCode.NO_CONTENT.value
    else:
        return '', HTTPStatusCode.BAD_REQUEST.value