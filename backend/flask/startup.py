from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import _config

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = _config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
