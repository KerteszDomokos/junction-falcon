from startup import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import RelationshipProperty
from sqlalchemy.dialects.mysql import (
    INTEGER,
    BIGINT,
    BOOLEAN,
    VARCHAR,
    CHAR,
)


class User(db.Model):
    id = db.Column(INTEGER, autoincrement=True, primary_key=True)
    email = db.Column(VARCHAR(254), unique=True, nullable=False)
    password_salt = db.Column(CHAR(64), nullable=False)
    password_hash = db.Column(CHAR(64), nullable=False)


class Session(db.Model):
    id = db.Column(INTEGER, autoincrement=True, primary_key=True)
    ip_address = db.Column(VARCHAR(15), nullable=True)
    token_hash = db.Column(CHAR(64), nullable=False)
    start_time = db.Column(BIGINT, server_default="0", nullable=False)
    user_id = db.Column(INTEGER, ForeignKey(User.id), nullable=True)
    user: User = RelationshipProperty(User, foreign_keys=[user_id])
    persistent = db.Column(BOOLEAN, server_default="0", nullable=False)