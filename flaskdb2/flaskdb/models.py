"""
A Sample Web-DB Application for DB-DESIGN lecture
Copyright (C) 2022 Yasuhiro Hayashi
"""
from calendar import THURSDAY
from locale import MON_1, MON_12
from flaskdb import db
from flask_login import UserMixin, LoginManager

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer)
    loginID = db.Column(db.Integer(), unique=True, nullable=False,primary_key=True)
    grade = db.Column(db.Integer(),nullable=False,primary_key=True)
    groupnumber = db.Column(db.Integer(),nullable=False,primary_key=True)
    username = db.Column(db.String(128),nullable=False,primary_key=True)
    password = db.Column(db.String(128),nullable=False)

    def __repr__(self):
        return "<User %r>" % self.id

class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.loginID"), nullable=False)
    itemname = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Integer(), nullable=False)

class Form1(db.Model):
    __tablename__ = "form1"
    id = db.Column(db.Integer,primary_key=True)
    loginID = db.Column(db.Integer,db.ForeignKey("users.loginID"),nullable=False,unique=True)
    mon_1 = db.Column(db.Integer,nullable=False)
    mon_2 = db.Column(db.Integer,nullable=False)
    mon_3 = db.Column(db.Integer,nullable=False)
    mon_4 = db.Column(db.Integer,nullable=False)
    mon_5 = db.Column(db.Integer,nullable=False)
    mon_6 = db.Column(db.Integer,nullable=False)
    tue_1 = db.Column(db.Integer,nullable=False)
    tue_2 = db.Column(db.Integer,nullable=False)
    tue_3 = db.Column(db.Integer,nullable=False)
    tue_4 = db.Column(db.Integer,nullable=False)
    tue_5 = db.Column(db.Integer,nullable=False)
    tue_6 = db.Column(db.Integer,nullable=False)
    wen_1 = db.Column(db.Integer,nullable=False)
    wen_2 = db.Column(db.Integer,nullable=False)
    wen_3 = db.Column(db.Integer,nullable=False)
    wen_4 = db.Column(db.Integer,nullable=False)
    wen_5 = db.Column(db.Integer,nullable=False)
    wen_6 = db.Column(db.Integer,nullable=False)
    thu_1 = db.Column(db.Integer,nullable=False)
    thu_2 = db.Column(db.Integer,nullable=False)
    thu_3 = db.Column(db.Integer,nullable=False)
    thu_4 = db.Column(db.Integer,nullable=False)
    thu_5 = db.Column(db.Integer,nullable=False)
    thu_6 = db.Column(db.Integer,nullable=False)
    fri_1 = db.Column(db.Integer,nullable=False)
    fri_2 = db.Column(db.Integer,nullable=False)
    fri_3 = db.Column(db.Integer,nullable=False)
    fri_4 = db.Column(db.Integer,nullable=False)
    fri_5 = db.Column(db.Integer,nullable=False)
    fri_6 = db.Column(db.Integer,nullable=False)

class Test(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.Integer)
    loginID = db.Column(db.Integer,db.ForeignKey("users.loginID"),nullable=False,primary_key=True)
    ss = db.Column(db.Integer,nullable=False)
    sao = db.Column(db.Integer,nullable=False)






    def __repr__(self):
        return "<Item %r>" % self.id
