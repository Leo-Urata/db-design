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



class Form1Form(FlaskForm):
    mon_1 = StringField(
        "mon_1",
        validators = [
            DataRequired(message="エラーが出た"),
        ],
    )
    mon_2 = StringField(
        "mon_2",
        validators = [
            DataRequired(message="エラーが出た"),
        ],
    )
    mon_3 = StringField(
        "mon_3",
        validators = [
            DataRequired(message="エラーが出た"),
        ],
    )
    mon_4 = StringField(
        "mon_4",
        validators = [
            DataRequired(message="エラーが出た"),
        ],
    )
    mon_5 = StringField(
        "mon_5",
        validators = [
            DataRequired(message="エラーが出た"),
        ],
    )
    mon_6 = StringField(
        "mon_6",
        validators = [
            DataRequired(message="エラーが出た"),
        ],
    )
    tue_1 = StringField(
        "tue_1",
        validators = [
            DataRequired(message="エラーが出た"),
        ],
    )
    tue_2 = StringField(
        "tue_2",
        validators = [
            DataRequired(message="エラーが出た"),
        ],
    )
    tue_3 = StringField(
        "tue_3",
        validators = [
            DataRequired(message="エラーが出た"),
        ],
    )
    tue_4 = StringField(
        "tue_4",
        validators = [
            DataRequired(message="エラーが出た"),
        ],
    )
    tue_5 = StringField(
        "tue_5",
        validators = [
            DataRequired(message="エラーが出た"),
        ],
    )
    tue_6 = StringField(
        "tue_6",
        validators = [
            DataRequired(message="エラーが出た"),
        ],
    )
    wen_1 = StringField(
        "wen_1",
        validators = [
            DataRequired(message="エラーが出た"),
        ],
    )
    wen_2 = StringField(
        "wen_2",
        validators = [
            DataRequired(message="エラーが出た"),
        ],
    )
    wen_3 = StringField(
        "wen_3",
        validators = [
            DataRequired(message="エラーが出た"),
        ],
    )
    wen_4 = StringField(
        "wen_4",
        validators = [
            DataRequired(message="エラーが出た"),
        ],
    )
    wen_5= StringField(
        "wen_5",
        validators = [
            DataRequired(message="エラーが出た"),
        ],
    )
    wen_6 = StringField(
        "wen_6",
        validators = [
            DataRequired(message="エラーが出た"),
        ],
    )
    thu_1 = StringField(
        "thu_1",
        validators = [
            DataRequired(message="エラーが出た"),
        ],
    )
    thu_2 = StringField(
        "thu_2",
        validators = [
            DataRequired(message="エラーが出た"),
        ],
    )
    thu_3 = StringField(
        "thu_3",
        validators = [
            DataRequired(message="エラーが出た"),
        ],
    )
    thu_4 = StringField(
        "thu_4",
        validators = [
            DataRequired(message="エラーが出た"),
        ],
    )
    thu_5 = StringField(
        "thu_5",
        validators = [
            DataRequired(message="エラーが出た"),
        ],
    )
    thu_6 = StringField(
        "thu_6",
        validators = [
            DataRequired(message="エラーが出た"),
        ],
    )
    fri_1 = StringField(
        "fri_1",
        validators = [
            DataRequired(message="エラーが出た"),
        ],
    )
    fri_2 = StringField(
        "fri_2",
        validators = [
            DataRequired(message="エラーが出た"),
        ],
    )
    fri_3 = StringField(
        "fri_3",
        validators = [
            DataRequired(message="エラーが出た"),
        ],
    )
    fri_4 = StringField(
        "fri_4",
        validators = [
            DataRequired(message="エラーが出た"),
        ],
    )
    fri_5 = StringField(
        "fri_5",
        validators = [
            DataRequired(message="エラーが出た"),
        ],
    )
    fri_6 = StringField(
        "fri_6",
        validators = [
            DataRequired(message="エラーが出た"),
        ],
    )
   
    cancel = ButtonField("Cencel")
    submit = SubmitField("Submit")

    def copy_from(self, form1):
        self.mon_1.data = form1.mon_1
        self.mon_2.data = form1.mon_2
        self.mon_3.data = form1.mon_3
        self.mon_4.data = form1.mon_4
        self.mon_5.data = form1.mon_5
        self.mon_6.data = form1.mon_6
        self.tue_1.data = form1.tue_1
        self.tue_2.data = form1.tue_2
        self.tue_3.data = form1.tue_3
        self.tue_4.data = form1.tue_4
        self.tue_5.data = form1.tue_5
        self.tue_6.data = form1.tue_6
        self.wen_1.data = form1.wen_1
        self.wen_2.data = form1.wen_2
        self.wen_3.data = form1.wen_3
        self.wen_4.data = form1.wen_4
        self.wen_5.data = form1.wen_5
        self.wen_6.data = form1.wen_6
        self.thu_1.data = form1.thu_1
        self.thu_2.data = form1.thu_2
        self.thu_3.data = form1.thu_3
        self.thu_4.data = form1.thu_4
        self.thu_5.data = form1.thu_5
        self.thu_6.data = form1.thu_6
        self.fri_1.data = form1.fri_1
        self.fri_2.data = form1.fri_2
        self.fri_3.data = form1.fri_3
        self.fri_4.data = form1.fri_4
        self.fri_5.data = form1.fri_5
        self.fri_6.data = form1.fri_6
 
        

    def copy_to(self, form1):
        form1.mon_1 = self.mon_1.data
        form1.mon_2 = self.mon_2.data
        form1.mon_3 = self.mon_3.data
        form1.mon_4 = self.mon_4.data
        form1.mon_5 = self.mon_5.data
        form1.mon_6 = self.mon_6.data
        form1.tue_1 = self.tue_1.data
        form1.tue_2 = self.tue_2.data
        form1.tue_3 = self.tue_3.data
        form1.tue_4 = self.tue_4.data
        form1.tue_5 = self.tue_5.data
        form1.tue_6 = self.tue_6.data
        form1.wen_1 = self.wen_1.data
        form1.wen_2 = self.wen_2.data
        form1.wen_3 = self.wen_3.data
        form1.wen_4 = self.wen_4.data
        form1.wen_5 = self.wen_5.data
        form1.wen_6 = self.wen_6.data
        form1.thu_1 = self.thu_1.data
        form1.thu_2 = self.thu_2.data
        form1.thu_3 = self.thu_3.data
        form1.thu_4 = self.thu_4.data
        form1.thu_5 = self.thu_5.data
        form1.thu_6 = self.thu_6.data
        form1.fri_1 = self.fri_1.data
        form1.fri_2 = self.fri_2.data
        form1.fri_3 = self.fri_3.data
        form1.fri_4 = self.fri_4.data
        form1.fri_5 = self.fri_5.data
        form1.fri_6 = self.fri_6.data
        


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
