from bson.objectid import ObjectId

class UserModel:
    def __init__(self, id=None, email=None, password=None):
        self.id = id
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email, 
            'password': self.password
        }
    
    def from_dict(dictionnary):
        if dictionnary['email'] is None or\
            dictionnary['password'] is None:
            return -1

        if dictionnary['_id'] is not None:
            if type(dictionnary['_id']) is ObjectId:
                return UserModel(str(dictionnary['_id']), dictionnary['email'], dictionnary['password'])
            else:
                return UserModel(dictionnary['_id'], dictionnary['email'], dictionnary['password'])

        elif dictionnary['id'] is not None:
            if type(dictionnary['id']) is ObjectId:
                return UserModel(str(dictionnary['id']), dictionnary['email'], dictionnary['password'])
            else:
                return UserModel(dictionnary['id'], dictionnary['email'], dictionnary['password'])