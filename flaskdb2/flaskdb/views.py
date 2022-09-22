"""
A Sample Web-DB Application for DB-DESIGN lecture
Copyright (C) 2022 Yasuhiro Hayashi
"""
#from msvcrt import open_osfhandle
from pipes import quote
from flask import Blueprint, request, session, render_template, redirect, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import pickle
import pandas as pd
import numpy as np

from flaskdb import apps, db, da
from flaskdb.models import User, Item, Form1,Test
from flaskdb.forms import LoginForm, AddItemForm, SearchItemForm, SignUpForm,Form1Form


app = Blueprint("app", __name__)



      
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')

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
        return redirect(url_for("app.calendar",grade=session["grade"] ,groupnumber=session["groupnumber"]))
    return render_template("login.html", form=form)

@app.route("/calendar",methods=["GET","POST"])
def calendar():
    form1 = Form1.query.all()
    userID = []
    mon_1 = []
    mon_2 = []
    mon_3 = []
    mon_4 = []
    mon_5 = []
    mon_6 = []
    tue_1 = []
    tue_2 = []
    tue_3 = []
    tue_4 = []
    tue_5 = []
    tue_6 = []
    wen_1 = []
    wen_2 = []
    wen_3 = []
    wen_4 = []
    wen_5 = []
    wen_6 = []
    thu_1 = []
    thu_2 = []
    thu_3 = []
    thu_4 = []
    thu_5 = []
    thu_6 = []
    fri_1 = []
    fri_2 = []
    fri_3 = []
    fri_4 = []
    fri_5 = []
    fri_6 = []
    for data in form1:
        userID.append(str(data.loginID))
        mon_1.append(str(data.mon_1))
        mon_2.append(str(data.mon_2))
        mon_3.append(str(data.mon_3))
        mon_4.append(str(data.mon_4))
        mon_5.append(str(data.mon_5))
        mon_6.append(str(data.mon_6))
        tue_1.append(str(data.tue_1))
        tue_2.append(str(data.tue_2))
        tue_3.append(str(data.tue_3))
        tue_4.append(str(data.tue_4))
        tue_5.append(str(data.tue_5))
        tue_6.append(str(data.tue_6))
        wen_1.append(str(data.wen_1))
        wen_2.append(str(data.wen_2))
        wen_3.append(str(data.wen_3))
        wen_4.append(str(data.wen_4))
        wen_5.append(str(data.wen_5))
        wen_6.append(str(data.wen_6))
        thu_1.append(str(data.thu_1))
        thu_2.append(str(data.thu_2))
        thu_3.append(str(data.thu_3))
        thu_4.append(str(data.thu_4))
        thu_5.append(str(data.thu_5))
        thu_6.append(str(data.thu_6))
        fri_1.append(str(data.fri_1))
        fri_2.append(str(data.fri_2))
        fri_3.append(str(data.fri_3))
        fri_4.append(str(data.fri_4))
        fri_5.append(str(data.fri_5))
        fri_6.append(str(data.fri_6))

    df = pd.DataFrame(mon_1,columns=['mon-1'],index=userID)

    df['mon-2'] = mon_2
    df['mon-3'] = mon_3
    df['mon-4'] = mon_4
    df['mon-5'] = mon_5
    df['mon-4'] = mon_4
    df['mon-5'] = mon_5
    df['mon-6'] = mon_6
    df['tue-1'] = tue_1
    df['tue-2'] = tue_2
    df['tue-3'] = tue_3
    df['tue-4'] = tue_4
    df['tue-5'] = tue_5
    df['tue-6'] = tue_6
    df['wen-1'] = wen_1
    df['wen-2'] = wen_2
    df['wen-3'] = wen_3
    df['wen-4'] = wen_4
    df['wen-5'] = wen_5
    df['wen-6'] = wen_6
    df['thu-1'] = thu_1
    df['thu-2'] = thu_2
    df['thu-3'] = thu_3
    df['thu-4'] = thu_4
    df['thu-5'] = thu_5
    df['thu-6'] = thu_6
    df['fri-1'] = fri_1
    df['fri-2'] = fri_2
    df['fri-3'] = fri_3
    df['fri-4'] = fri_4
    df['fri-5'] = fri_5
    df['fri-6'] = fri_6

    df[['mon-1','mon-2','mon-3','mon-4','mon-5','mon-6','tue-1','tue-2','tue-3','tue-4','tue-5','tue-6','wen-1','wen-2','wen-3','wen-4','wen-5','wen-6','thu-1','thu-2','thu-3','thu-4','thu-5','thu-6','fri-1','fri-2','fri-3','fri-4','fri-5','fri-6']] = df[['mon-1','mon-2','mon-3','mon-4','mon-5','mon-6','tue-1','tue-2','tue-3','tue-4','tue-5','tue-6','wen-1','wen-2','wen-3','wen-4','wen-5','wen-6','thu-1','thu-2','thu-3','thu-4','thu-5','thu-6','fri-1','fri-2','fri-3','fri-4','fri-5','fri-6']].astype(int)
    df2 = df.T
    # df2.sum(axis = 'columns')

    df2['sum'] = df2.sum(axis =1)

    # print(df2[df2['sum']>4])
    # print(df2['sum']>4)
    dos = len(df['mon-1'])
    reqd_Index = df2[df2['sum']>=dos].index.tolist()

    d={'mon-1':'08:50~10:30', 'mon-2':'10:40~12:20','mon-3':'13:10~14:50','mon-4':'15:00~16:40','mon-5':'16:50~18:30','mon-6':'18:40~20:20',
    'tue-1':'08:50~10:30', 'tue-2':'10:40~12:20','tue-3':'13:10~14:50','tue-4':'15:00~16:40','tue-5':'16:50~18:30','tue-6':'18:40~20:20',
    'wen-1':'08:50~10:30', 'wen-2':'10:40~12:20','wen-3':'13:10~14:50','wen-4':'15:00~16:40','wen-5':'16:50~18:30','wen-6':'18:40~20:20',
    'thu-1':'08:50~10:30', 'thu-2':'10:40~12:20','thu-3':'13:10~14:50','thu-4':'15:00~16:40','thu-5':'16:50~18:30','thu-6':'18:40~20:20',
    'fri-1':'08:50~10:30', 'fri-2':'10:40~12:20','fri-3':'13:10~14:50','fri-4':'15:00~16:40','fri-5':'16:50~18:30','fri-6':'18:40~20:20'}
    pp = []
    ss = []
    for i in reqd_Index:
        pp.append(i)
        ss.append(d[i])

    mond = []
    tusd = []
    wend = []
    thur = []
    frid = []
    for j in pp:
        if 'mon' in j:
            mond.append(j)
        if 'tue' in j:
            tusd.append(j)
        if 'wen' in j:
            wend.append(j)
        if 'thu' in j :
            thur.append(j)
        if 'fri' in j :
            frid.append(j)
    sssl=[]
    pso = []
    sssf =[]
    ssds = []
    sssd = []
    for q in mond:
        sssl.append(d[q])
    for q in tusd:
        pso.append(d[q])
    for q in wend:
        sssf.append(d[q])
    for q in thur:
        ssds.append(d[q])
    for q in frid:
        sssd.append(d[q])


    i1 = sssl*7
    i1.sort()
    i2 = pso*7
    i2.sort()
    i3 = sssf*7
    i3.sort()
    i4 = ssds*7
    i4.sort()
    i5 = sssd*7
    i5.sort()


    montt = ['2022-09-26','2022-10-03','2022-10-17','2022-10-24','2022-10-31','2022-11-07','2022-11-14']
    tuett = ['2022-09-27','2022-10-04','2022-10-11','2022-10-18','2022-10-25','2022-11-01','2022-11-08']
    wentt = ['2022-09-28','2022-10-05','2022-10-12','2022-10-19','2022-10-26','2022-11-02','2022-11-09']
    thutt = ['2022-09-29','2022-10-06','2022-10-13','2022-10-20','2022-10-27','2022-11-03','2022-11-10']
    fritt = ['2022-09-23','2022-09-30','2022-10-14','2022-10-21','2022-10-28','2022-11-04','2022-11-11']
    kk = []
    for i in pp:
        if 'mon' in i:
            kk.extend(montt)
        if 'tue' in i:
            kk.extend(tuett)
        if 'wen' in i:
            kk.extend(wentt)
        if 'thu' in i:
            kk.extend(thutt)
        if 'fri' in i:
            kk.extend(fritt)

    u1 = i1 + i2 + i3 + i4 + i5

    events = []
    for (titles,date) in zip(u1,kk):
        events.append(
                {
                    "title": titles,
                    "date": date
                }
                
        )

    return render_template('calendar.html',events=events)



@app.route("/form1", methods=["GET", "POST"])
def form1():
    if request.method =='POST':
        name = request.form.getlist('checkbox')
        pp = []
        pp.clear()
        for x in range(1,31):
            if str(x) in name:
                pp.append(1)
            else:
                pp.append(0)
        ss = Form1(loginID=session['loginID'],mon_1=pp[0],
            mon_2=pp[1],
            mon_3=pp[2]
            ,mon_4=pp[3]
            ,mon_5=pp[4],
            mon_6=pp[5],
            tue_1=pp[6],
            tue_2=pp[7],
            tue_3=pp[8],
            tue_4=pp[9],
            tue_5=pp[10],
            tue_6=pp[11],
            wen_1=pp[12],
            wen_2=pp[13],
            wen_3=pp[14],
            wen_4=pp[15],
            wen_5=pp[16],
            wen_6=pp[17],
            thu_1=pp[18],
            thu_2=pp[19],
            thu_3=pp[20],
            thu_4=pp[21],
            thu_5=pp[22],
            thu_6=pp[23],
            fri_1=pp[24],
            fri_2=pp[25],
            fri_3=pp[26],
            fri_4=pp[27],
            fri_5=pp[28],
            fri_6=pp[29],
            )

        db.session.add(ss)
        db.session.commit()
            # #db.session.bulk_save_objects(user, update_changed_only=False)
            # #flash('Congratulations, you are now a registered user!')

        return redirect(url_for('app.calendar'))
    if request.method=='GET':

        return render_template('form.html')





@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop("loginID", None)
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("app.index"))

@app.route("/additem", methods=["GET", "POST"])
def additem():
    if not "loginID" in session:
        flash("Log in is required.", "danger")
        return redirect(url_for("app.login"))

    form = AddItemForm()

    if form.validate_on_submit():
        item = Item()
        form.copy_to(item)
        user = User.query.filter_by(username=session["loginID"]).first()
        item.user_id = user.id
        db.session.add(item)
        db.session.commit()

        flash("An item was added.", "info")
        return redirect(url_for("app.additem"))

    itemlist = Item.query.all()
    return render_template("additem.html", form=form, itemlist=itemlist)

@app.route("/searchitem", methods=["GET", "POST"])
def searchitem():
    if not "loginID" in session:
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

    if "itemlist" in session:
        itemlist = session["itemlist"]
        itemlist = pickle.loads(itemlist)
        session.pop("itemlist", None)
    else:
        itemlist = None
    
    return render_template("search.html", form=form, itemlist=itemlist)

    return render_template("search.html", form=form)

@app.route("/nativesql", methods=["GET", "POST"])
def nativesql():
    if not "loginID" in session:
        flash("Log in is required.", "danger")
        return redirect(url_for("app.login"))

    form = AddItemForm()

    if form.validate_on_submit():
        item = Item()
        form.copy_to(item)
        user = User.query.filter_by(username=session["loginID"]).first()
        item.user_id = user.id
        da.add_item(item)

        flash("An item was added.", "info")
        return redirect(url_for("app.additem"))

    itemlist = da.search_items()
    return render_template("additem.html", form=form, itemlist=itemlist)


