from bson.objectid import ObjectId
from .database import Database

db = Database.get_connection()
movies = db['movies']

class MovieDB:
    def find_all():
        return movies.find()

    def find_by_id(id):
        return movies.find_one({ '_id': ObjectId(id) })

    def insert(movie):
        result = movies.insert_one(movie)
        return result.inserted_id
    
    def update(id, movie):
        result = movies.update_one({'_id': ObjectId(id)}, {'$set': movie})
        return result.modified_count
    
    def delete(id):
        result = movies.delete_one({'_id': ObjectId(id)})
        return result.deleted_count == 1