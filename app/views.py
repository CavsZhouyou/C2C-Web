from app import app 
from flask import request,flash,redirect,session,g,jsonify
from .models import *
import re 
@app.route('/')
def index():
    return "HelloWorld"

@app.before_request
def before_request():
    if 'user' in session:
        g.current_user = User.query.filter_by(
                user_id=session['user']).one()
    else:
        g.current_user=None 

@app.route('/login',methods=['POST','GET'])
def login():
    if g.current_user:
        flash("您已经登录")
        return redirect('/')
    if request.method=="GET":
        return app.send_satic_file('login.html')
    else: 
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.usercheck(email,password)
        if user:
            session['user'] = user.user_id 
            return "{success:True}"
        else:
            return "{success:False}"

@app.route('/registe',methods=['POST','GET'])
def registe():
    if g.current_user:
        flash("您已经登录")
        return redirect('/')
    if request.method=="GET"
        return app.send_satic_file('registe.html')
    else:
        #TO-DO
        #获取表格信息，填充一个user对象
        if User.useradd(user):
            return "{success:True}"
        else:
            return "{success:False}"

@app.route('/logout',methods=['GET','POST'])
def logout():
    session.pop('user',None)
    g.current_user=None 
    return redirect('/login')

@app.route('/userinfo',methods=['GET','POST'])
def userinfo()
    if g.current_user:
        return g.current_user.getuserinfo()
    else:
        return jsonify({'success':False})

