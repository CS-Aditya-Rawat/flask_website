from flask import Blueprint
from . import db
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy.sql import func

models = Blueprint('models', __name__)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password =  db.Column(db.String(150), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    name = db.Column(db.String(150))
    
    notes = db.relationship('Note')

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone = True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


