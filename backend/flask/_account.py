from _models import db, User, Session

def create_user(
    json: dict,
):
    """
    Create a new user and add them to the database.

    returns: User
    """
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

