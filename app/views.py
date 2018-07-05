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
        return g.current_user.to_json()
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

@app.route('/accommodation/list/', methods=['GET', 'POST'])
def accommodation():
    dic = request.get_json()
    if 'index' in dic:
        index = dic['index']
        return_dic = {}
        if isinstance(index, int) and index > 0:
            index = index * 10
            accommodations = Accommodation.query.all()[index - 10:index - 1]
            for one_acc in accommodations:
                return_dic[one_acc.acc_id] = {one_acc.acc_description, one_acc.acc_area, one_acc.acc_price,images}
            return jsonify(return_dic)
    else:
        return jsonify({'success': False})

@app.route('/accommodation/image/<int:acc_id>',methods=['GET'])
def accommodation_id_image(acc_id):
    images = AccommodationImage.query.filter(accImage_acc_id=acc_id).all()
    if images:
        i = 0
        dic={}
        for image in images:
            dic[i] = image.accImage_url
            i+=1
        return jsonify(dic)
    else:
        return jsonify({'success': False})


@app.route('/accommodation/<int:acc_id>', methods=['GET'])
def accommodation_id(acc_id):
    one_acc = Accommodation.query.get(acc_id)
    if one_acc:
        return app.send_satic_file('accommodation_info.html')
    else:
        return app.send_static_file('404.html')

@app.route('/accommodation/show/<int:acc_id>', methods=['GET'])
def accommodation_id_info(acc_id):
    one_acc = TravelMessage.query.get(acc_id)
    if one_acc:
        return one_acc.to_json()
    else:
        return jsonify({'success': False})

@app.route('/accommodation/add',methods=['GET','POST'])
def accommodation_add():
    data=request.get_json()
    oneAcc = Accommodation(
        acc_address = data['acc_address'],
        acc_capacity = data['acc_capacity'],
        acc_price = data['acc_price'],
        acc_area = data['acc_area'],
        acc_description = data['acc_description'],
        acc_user_id = data['acc_user_id'],
        acc_type_id = data['acc_type_id'],
        oneAcc.acc_city = data['acc_city']
    )
    try:
        db.session.add(oneAcc)
        db.session.commit()
        return jsonify({'success':True})
    except Exception:
        return jsonify({'success':False})

@app.route('/del_one_accommodation/<int:acc_id>')
def del_one_accommodation(acc_id):
    if g.current_user.role_id != 1:
        return jsonify({'success':False})
    oneAcc = Accommodation.query.get(acc_id)
    if oneAcc:
        try:
            db.session.delete(oneAcc)
            db.session.commit()
            return jsonify({'success':True})
        except Exception:
            return jsonify({'success':False})
    else:
        return jsonify({'success':False})


@app.route('/accommodation/delete/<int:acc_id>',methods=['GET'])
def accommodation_delete(acc_id):
    #判断是否是出租者
    if g.current_user.role_id != 2:
        return jsonify({'success': False})
    #判断是否是出租者拥有的房源
    oneAcc=Accommodation.query.get(acc_id)
    if oneAcc:
        if oneAcc.acc_user_id != g.current_user.user_id:
            jsonify({'success': False})
    else:
        return jsonify({'success': False})

    #删除房源
    if oneAcc:
        try:
            db.session.delete(oneAcc)
            db.session.commit()
            return jsonify({'success': True})
        except Exception:
            return jsonify({'success': False})
    else:
        return jsonify({'success': False})

@app.route('/accommodation/update/',methods=['GET','POST'])
def accommodation_update():
    # 判断是否是出租者
    if g.current_user.role_id != 2:
        return jsonify({'success': False})
    # 判断是否是出租者拥有的房源
    data = request.get_json()
    oneAcc = Accommodation.query.get(data['acc_id'])
    if oneAcc:
        if oneAcc.acc_user_id != g.current_user.user_id:
            jsonify({'success': False})
    else:
        return jsonify({'success': False})

    #修改房源
    if oneAcc:
        oneAcc.acc_address = data['acc_address']
        oneAcc.acc_capacity = data['acc_capacity']
        oneAcc.acc_price = data['acc_price']
        oneAcc.acc_area = data['acc_area']
        oneAcc.acc_description = data['acc_description']
        oneAcc.acc_user_id = data['acc_user_id']
        oneAcc.acc_type_id = data['acc_type_id']
        oneAcc.acc_city = data['acc_city']
        try:
            db.session.commit()
        except Exception:
            return jsonify({'success': False})
    else:
        return jsonify({'success': False})    
