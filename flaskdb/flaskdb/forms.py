"""
A Sample Web-DB Application for DB-DESIGN lecture
Copyright (C) 2022 Yasuhiro Hayashi
"""
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length
from flaskdb.widgets import ButtonField
from wtforms import validators
from typing import Optional

class LoginForm(FlaskForm):
    loginID = StringField(
        "loginID",
        validators = [
            DataRequired(message="学籍番号を入力してください"),
            length(max=7, message="User Name should be input within 64 characters."),
        ],
    )
    grade = StringField(
        "grade",
        validators = [
            validators.Optional(),
        ],
    )
    groupnumber = StringField(
        "groupnumber",
        validators = [
           validators.Optional(),
        ],
    )
    username = StringField(
        "User Name",
        validators = [
           validators.Optional(),
        ],
    )
    password = PasswordField(
        "Password",
        validators = [
            DataRequired(message="パスワードを入力してください"),
        ],
    )
    cancel = ButtonField("Cancel")
    submit = SubmitField("Login")

    def copy_from(self, user):
        self.loginID.data = user.loginID
        # self.grade.data = user.grade
        # self.groupnumber.data = user.groupnumber
        # self.username.data = user.username
        self.password.data = user.password

    def copy_to(self, user):
        user.loginID = self.loginID.data
        # user.grade = self.grade.data
        # user.groupnumber = self.gropunumber.data
        # user.username = self.username.data
        user.password = self.password.data



class SignUpForm(FlaskForm):
    loginID = StringField(
        "loginID",
        validators = [
            DataRequired(message="学籍番号を入力してください"),
            length(min=7,max=7, message="入力されたものは学籍番号ではありません"),
            validators.Regexp('[0-9]', message='数値を入力してください')
        ],
    )
    grade = StringField(
        "grade",
        validators = [
            DataRequired(message="学年を入力してください"),
        ],
    )
    groupnumber = StringField(
        "groupnumber",
        validators = [
            DataRequired(message="グループナンバーを入力してください"),
        ],
    )
    username = StringField(
        "username",
        validators = [
            DataRequired(message="ユーザー名を入力してください"),
        ],
    )
    password = PasswordField(
        "Password",
        validators = [
            DataRequired(message="パスワードを入力してください。"),
        ],
    )
    cancel = ButtonField("Cencel")
    submit = SubmitField("Submit")

    def copy_from(self, user):
        self.loginID.data = user.loginID
        self.grade.data = user.grade
        self.groupnumber.data = user.groupnumber
        self.username.data = user.username
        self.password.data = user.password

    def copy_to(self, user):
        user.loginID = self.loginID.data
        user.grade = self.grade.data
        user.groupnumber = self.groupnumber.data
        user.username = self.username.data
        user.password = self.password.data

class AddItemForm(FlaskForm):
    itemname = StringField(
        "Item Name",
        validators = [
            DataRequired(message="Item Name is required."),
        ],
    )
    price = IntegerField(
        "Price",
        validators = [
            DataRequired(message="Price is required."),
        ],
    )
    cancel = ButtonField("Cencel")
    submit = SubmitField("Submit")

    def copy_from(self, item):
        self.itemname.data = item.itemname
        self.price.data = item.price

    def copy_to(self, item):
        item.itemname = self.itemname.data
        item.price = self.price.data

class SearchItemForm(FlaskForm):
    itemname = StringField(
        "Item Name",
        validators = [
            DataRequired(message="Item Name is required."),
        ],
    )
    cancel = ButtonField("Cencel")
    submit = SubmitField("Submit")

    def copy_from(self, item):
        self.itemname.data = item.itemname

    def copy_to(self, item):
        item.itemname = self.itemname.data
