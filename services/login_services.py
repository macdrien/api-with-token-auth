import datetime

from flask_jwt_extended import create_access_token

from common.password_manager import PassowordManager
from database.user_db import UserDB
from models.user_model import UserModel

class LoginServices:
    def get_all():
        result = UserDB.find_all()
        users = []

        for user in result:
            users.append(user.to_dict())

        return users

    def create_user(user_to_create):
        user_to_create.password = PassowordManager.hash_password(user_to_create.password)
        created_user = { '_id': str(UserDB.insert(user_to_create.to_dict()))}
        return created_user

    def login(user_to_login):
        user_in_database = UserDB.find_by_email(user_to_login['email'])
        is_authorized = PassowordManager.check_password(user_in_database.password, user_to_login['password'])

        if not is_authorized:
            return None
        
        expires = datetime.timedelta(days=15)
        return create_access_token(identity=user_in_database.id, expires_delta=expires)