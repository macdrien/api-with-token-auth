from pymongo import MongoClient

class Database:
    def get_connection():
        return MongoClient('mongodb://mongo:27017')['movie-bag']