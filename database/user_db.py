from bson.objectid import ObjectId
from .database import Database
from models.user_model import UserModel

db = Database.get_connection()
users = db['users']

class UserDB:
    def find_all():
        result = users.find()
        user_list = []
        for user in result:
            user_to_add = UserModel.from_dict(user)
            user_list.append(user_to_add)
        return user_list

    def find_by_id(id):
        result = users.find_one({ '_id': ObjectId(id) })
        user = UserModel.from_dict(result)
        return user

    def find_by_email(email):
        result = users.find_one({ 'email': email })
        user = UserModel.from_dict(result)
        return user

    def insert(user):
        result = users.insert_one(user)
        return result.inserted_id
    
    def update(id, user):
        result = users.update_one({'_id': ObjectId(id)}, {'$set': user})
        return result.modified_count
    
    def delete(id):
        result = users.delete_one({'_id': ObjectId(id)})
        return result.deleted_count == 1