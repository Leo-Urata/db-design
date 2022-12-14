"""
A Sample Web-DB Application for DB-DESIGN lecture
Copyright (C) 2022 Yasuhiro Hayashi
"""
from flask import Blueprint, request, session, render_template, redirect, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import pickle

from flaskdb import apps, db, da
from flaskdb.models import User, Item
from flaskdb.forms import LoginForm, AddItemForm, SearchItemForm, SignUpForm

app = Blueprint("app", __name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("/index.html")

@app.route("/now", methods=["GET", "POST"])
def now():
    return str(datetime.datetime.now())

# This is a very danger method
# @app.route("/receive", methods=["GET", "POST"])
# def receive():
#     if request.method == "GET":
#         username = request.args.get("username")
#         password = request.args.get("password")
#     else:
#         username = request.form["username"]
#         password = request.form["password"]

#     return render_template("receive.html", username=username, password=password)

@app.route("/initdb", methods=["GET", "POST"])
def initdb():
    db.drop_all()
    db.create_all()
    
    keita = User(loginID=2022038,grade=3,groupnumber=1, username="keita", password="password")
    db.session.add(keita)
    db.session.commit()
    return "initidb() method was executed. "

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()

    if form.validate_on_submit():
        grade = request.form.get('grade')
        groupnumber = request.form.get('groupnumber')
        user = User(loginID=form.loginID.data,grade=grade,groupnumber=groupnumber,username=form.username.data,password=form.password.data)
        # Userのインスタンスを作成
        db.session.add(user)
        #db.session.bulk_save_objects(user, update_changed_only=False)
        db.session.commit()
        #flash('Congratulations, you are now a registered user!')
        return redirect(url_for('app.login'))
  # ユーザーが未ログインまたはバリデーションエラーの場合、ユーザー登録ページにリダイレクト
    return render_template('signup.html', form=form)
   

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # print(form.loginID.data)
        # print(form.password.data)
        user = User.query.filter_by(loginID=form.loginID.data).first()

        if user is None or user.password != form.password.data:
            flash("loginID or Password is incorrect.", "danger")
            return redirect(url_for("app.login"))


        session["loginID"] = user.loginID
        session["name"] = user.username
        session["grade"] = user.grade
        session["groupnumber"] = user.groupnumber
        # userinfo = User.query.filter(User.loginID.like("%" + form.loginID.data + "%")).all()  
        return redirect(url_for("app.index"))
    return render_template("login.html", form=form)

@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop("loginID", None)
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("app.index"))

@app.route("/additem", methods=["GET", "POST"])
def additem():
    if not "username" in session:
        flash("Log in is required.", "danger")
        return redirect(url_for("app.login"))

    form = AddItemForm()

    if form.validate_on_submit():
        item = Item()
        form.copy_to(item)
        user = User.query.filter_by(username=session["username"]).first()
        item.user_id = user.id
        db.session.add(item)
        db.session.commit()

        flash("An item was added.", "info")
        return redirect(url_for("app.additem"))

    itemlist = Item.query.all()
    return render_template("additem.html", form=form, itemlist=itemlist)

@app.route("/searchitem", methods=["GET", "POST"])
def searchitem():
    if not "username" in session:
        flash("Log in is required.", "danger")
        return redirect(url_for("app.login"))

    form = SearchItemForm()

    if form.validate_on_submit():
        itemlist = Item.query.filter(Item.itemname.like("%" + form.itemname.data + "%")).all()        
        return render_template("search.html", form=form, itemlist=itemlist)

        # For change to PRG
        # itemlist = pickle.dumps(itemlist)
        # session["itemlist"] = itemlist
        # return redirect(url_for("app.searchitem"))

    # if "itemlist" in session:
    #     itemlist = session["itemlist"]
    #     itemlist = pickle.loads(itemlist)
    #     session.pop("itemlist", None)
    # else:
    #     itemlist = None
    # 
    # return render_template("search.html", form=form, itemlist=itemlist)

    return render_template("search.html", form=form)

@app.route("/nativesql", methods=["GET", "POST"])
def nativesql():
    if not "username" in session:
        flash("Log in is required.", "danger")
        return redirect(url_for("app.login"))

    form = AddItemForm()

    if form.validate_on_submit():
        item = Item()
        form.copy_to(item)
        user = User.query.filter_by(username=session["username"]).first()
        item.user_id = user.id
        da.add_item(item)

        flash("An item was added.", "info")
        return redirect(url_for("app.additem"))

    itemlist = da.search_items()
    return render_template("additem.html", form=form, itemlist=itemlist)


