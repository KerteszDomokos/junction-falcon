from os import abort
from _models import db, User, Session
from secrets import token_hex
from hashlib import sha256

def create_user(json: dict):
    if "email" in json and "password_hash" in json:
        print ("Valid request")
        password=json["password_hash"]
        password_salt = token_hex(32)
        password_hash = sha256((password + password_salt).encode("ascii")).hexdigest()
        
        user=User(email=json["email"], password_hash=password_hash,password_salt=password_salt)
        db.session.add(user)
        db.session.commit()
    else:
        print("[/user] Not valid request: keys error")
        abort
    
    return user


def auth_password(json: dict):
    """
    Authenticate a user by email and password.

    returns: User
    """

    return user


def auth_session(json: dict = None, session_token: str = None):
    """
    Authenticate a user by session token. If json is None, the "Session-Token" header
    will be used.

    returns: Session
    """

    return session


def create_session(user: User, json: dict, ip_address: str = None):
    """
    Create a new session for a user with a hashed session key and store it in db.

    returns: session key (non-hashed)
    """

    return session_token


def delete_session(session: Session):
    """
    Deletes a session.
    """


def change_password(session: Session):
    """
    Update user password
    """

