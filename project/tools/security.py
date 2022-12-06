import base64
import calendar
import datetime
import hashlib
from os import abort

import jwt
from flask import current_app



def __generate_password_digest(password: str) -> bytes:
    return hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password.encode("utf-8"),
        salt=current_app.config["PWD_HASH_SALT"],
        iterations=current_app.config["PWD_HASH_ITERATIONS"],
    )


def generate_password_hash(password: str) -> str:
    return base64.b64encode(__generate_password_digest(password)).decode('utf-8')


def compare_password_hash(password_hash, other_password):
    if password_hash == generate_password_hash(other_password):
        return True


class AuthsService:
    def __init__(self, users_service):
        self.users_service = users_service
        
    
    def generate_tokens(self, email, password, is_refresh=False):
        user = self.users_service.get_user_by_login(email)
        
        if user is None:
            raise abort(404)
        
        if not is_refresh:
            if not compare_password_hash(user.password, password):
                abort(400)
                
        data = {
            "email": email,
            "password": password
        }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=current_app.config['TOKEN_EXPIRE_MINUTES'])
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, key=current_app.config['SECRET_KEY'], algorithm=current_app.config['ALGORITHM'])
        
        days130 = datetime.datetime.utcnow() + datetime.timedelta(minutes=current_app.config['TOKEN_EXPIRE_DAYS'])
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, key=current_app.config['SECRET_KEY'], algorithm=current_app.config['ALGORITHM'])
        return {"access_token": access_token, "refresh_token": refresh_token}
    
    
    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(jwt=refresh_token, key=current_app.config['SECRET_KEY'], algorithm=current_app.config['ALGORITHM'])
        email = data.get("email")
        return self.generate_tokens(email, None, is_refresh=True)