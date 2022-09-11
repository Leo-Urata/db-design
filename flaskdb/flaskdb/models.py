"""
A Sample Web-DB Application for DB-DESIGN lecture
Copyright (C) 2022 Yasuhiro Hayashi
"""
from flaskdb import db
from flask_login import UserMixin, LoginManager

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    loginID = db.Column(db.Integer(), unique=True, nullable=False,primary_key=True)
    grade = db.Column(db.Integer(),nullable=False)
    # groupnumber = db.Column(db.Integer(),nullable=False)
    # username = db.Column(db.String(128),nullable=False)
    groupnumber = db.Column(db.Integer(),nullable=False)
    username = db.Column(db.String(128),nullable=False)
    password = db.Column(db.String(128),nullable=False)

    def __repr__(self):
        return "<User %r>" % self.id

class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    itemname = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return "<Item %r>" % self.id
