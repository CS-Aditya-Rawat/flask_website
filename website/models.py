from flask import Blueprint
from . import db
from datetime import datetime
from flask_login import UserMixin

models = Blueprint('models', __name__)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password =  db.Column(db.String(150), nullable=False)
    name = db.Column(db.String(150))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def password(self):
        raise AttributeError("Password is not a ")
