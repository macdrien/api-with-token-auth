from flask_bcrypt import generate_password_hash, check_password_hash

class PassowordManager:
    def hash_password(password_to_hash):
        return generate_password_hash(password_to_hash).decode('utf8')
    
    def check_password(saved_password, password_to_check):
        return check_password_hash(saved_password, password_to_check)