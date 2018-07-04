from app import app 
from flask import request,flash,redirect,session,g,jsonify
from .models import *
import json 
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
            return jsonify({'success':True})
        else:
            return jsonify({'success':False})

@app.route('/registe',methods=['POST','GET'])
def registe():
    if g.current_user:
        flash("您已经登录")
        return redirect('/')
    if request.method=="GET":
        return app.send_satic_file('registe.html')
    else:
        #TO-DO
        #获取表格信息，填充一个user对象
        if User.useradd(user):
            return jsonify({'success':True})
        else:
            return jsonify({'success':False})

@app.route('/logout',methods=['GET','POST'])
def logout():
    session.pop('user',None)
    g.current_user=None 
    return redirect('/login')

@app.route('/userinfo',methods=['GET','POST'])
def userinfo():
    if g.current_user:
        return g.current_user.getuserinfo()
    else:
        return jsonify({'success':False})

@app.route('/travelmessage/list/',methods=['GET','POST'])
def travelmessage():
    dic = request.get_json()
    if 'index' in dic:
        index = dic['index']
        return_dic={}
        if isinstance(index,int) and index>0:
            index=index*10 
            travelmessages = TravelMessage.query.order_by(
        TravelMessage.date.desc()).all()[index-10:index-1]
            for tm in travelmessages:
                return_dic[tm.tmessage_id] = {tm.title,tm.date,tm.addressOftravel}

            return jsonify(return_dic)
    else:
        return jsonify({'success':False}) 

@app.route('/travelmessage/<int:tm_id>',methods=['GET'])
def travelmessage_id(tm_id):
    tm = TravelMessage.query.get(tm.id)
    if tm:
        return app.send_satic_file('travelmessage_info.html')
    else:
        return app.send_static_file('404.html')

@app.route('/travelmessage/show/<int:tm_id>',methods=['GET'])
def travelmessage_id_info(tm_id):
    tm = TravelMessage.query.get(tm.id)
    if tm:
        return tm.to_json()
    else:
        return jsonify({'success':False}) 
    
