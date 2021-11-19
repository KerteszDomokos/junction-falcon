from flask import request, abort
from startup import app
from _models import Session, User
import _account
import _types


@app.route("/register", methods=["POST"])
def register():
    apikey = request.headers.get("X-Api-Key")
    if apikey is None or apikey != "your_api_key":
        abort(401)
    user: User = _account.create_user(json=request.json)
    session_token = _account.create_session(user, request.remote_addr)
    return _types.success_response(
        {"email": user.email, "sessionToken": session_token}
    )


@app.route("/login", methods=["POST"])
def login():
    user: User = _account.auth_password(request.json)
    session_token = _account.create_session(user, request.json, request.remote_addr)
    return _types.success_response(
        {"email": user.email, "sessionToken": session_token}
    )


@app.route("/logout", methods=["POST"])
def logout():
    session: Session = _account.auth_session(request.json)
    _account.delete_session(session)
    return _types.success_response("logged out")


@app.route("/change-password", methods=["PATCH"])
def change_password():
    session: Session = _account.auth_session()
    _account.change_password(session)
    return _types.success_response("password changed")
