from startup import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import RelationshipProperty
from sqlalchemy.dialects.mysql import (
    INTEGER,
    TEXT
)


class User(db.Model):
    id = db.Column(INTEGER, autoincrement=True, primary_key=True)
    email = db.Column(TEXT, unique=True, nullable=False)
    password_salt = db.Column(TEXT, nullable=False)
    password_hash = db.Column(TEXT, nullable=False)


class Session(db.Model):
    id = db.Column(INTEGER, autoincrement=True, primary_key=True)
    ip_address = db.Column(TEXT, nullable=True)
    token_hash = db.Column(TEXT, nullable=False)
    start_time = db.Column(INTEGER, server_default="0", nullable=False)
    user_id = db.Column(INTEGER, ForeignKey(User.id), nullable=True)
    user: User = RelationshipProperty(User, foreign_keys=[user_id])
    persistent = db.Column(TEXT, server_default="0", nullable=False)