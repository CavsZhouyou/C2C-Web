from app import app,qiniu_handle,bucket_name,policy,bucket_domain
from datetime import datetime
from flask import request,flash,redirect,session,g,jsonify 
from .models import *
import json 
import re 

@app.route('/')
def index():
    return jsonify({'success':True})

@app.before_request
def before_request():
    if 'user' in session:
        g.current_user = User.query.filter_by(
                user_id=session['user']).one()
    else:
        g.current_user=None 

@app.route('/c2c/login',methods=['POST','GET'])
def login():
    if g.current_user:
        return jsonify({'success':False,
                     'error':"Alreadylogin"})
    else:
        data = request.get_json()
        if(data==None or 'email' not in data or 'password' not in data):
            return jsonify({'success':False,
                            'error':"WrongDataFormat"})
        email = data['email']
        password = data['password']
        user = User.usercheck(email,password)
        if user:
            session['user'] = user.user_id 
            return jsonify({'success':True,
                            'user_id':user.user_id,
                            'role_id':user.role_id})
        else:
            return jsonify({'success':False,
                            'error':'WrongUsernameOrPassWord'})
#注册请求
@app.route('/c2c/regist',methods=['POST','GET'])
def registe():
    if g.current_user:
        return redirect('/')
    else:
        dic = request.get_json()
        try:
            user = User(
                    nickname=dic['nickname'], 
                    password=dic['password'],
                    email = dic['email'],
                    phone = dic['phone'],
                    role_id = dic['role_id'],
                    name = dic['name'],
                    id_card = dic['id_card']
                    )
        except:
            return jsonify({'success':False,
                            'error':'WrongDataFormat'})
        if User.useradd(user):
            return jsonify({'success':True})
        else:
            return jsonify({'success':False,
                            'error':'DB add error'})


#用户信息修改
@app.route('/c2c/userupdate',methods=['POST','GET'])
def userupdate():
    if g.current_user:
        try:
            user = User.query.get(g.current_user.user_id)
            data = request.get_json()
            user.nickname = data['nickname']
            user.phone = data['phone']
            user.info = data['info']
            db.session.commit()
            return jsonify({'success':True})
        except Exception:
            return jsonify({'success':False,
                            'error':"Change Failed"})
    else:
        return jsonify({'success':False,
                        'error':'Not Login'})
#密码修改
@app.route('/c2c/changepassword',methods=['POST','GET'])
def userpasswordchange():
    if g.current_user:
        try:
            user = User.query.get(g.current_user.user_id)
            data = request.get_json()
            if(('password' in data) and ('old_password' in data) and len(data['password'])<5 and len(data['password'])>20):
                return jsonify({'success':False,
                                'error':"Empty or Break  Length limit"})
            if(data['old_password']!= user.password):
                return jsonify({'success':False,
                                'error':"原始密码错误"})   
            user.password = data['password']
            db.session.commit()
            return jsonify({'success':True})
        except Exception as e:
            print(e)
            return jsonify({'success':False,
                            'error':"Change Failed"})
    else:
        return jsonify({'success':False,
                        'error':'Not Login'})


#登出请求
@app.route('/c2c/logout',methods=['GET','POST'])
def logout():
    try:
        session.pop('user',None)
        g.current_user=None
        return jsonify({'success':True})
    except Exception:
        return jsonify({'success':False})

#用户信息获取接口
@app.route('/c2c/userinfo',methods=['GET','POST'])
def userinfo():
    if g.current_user:
        return g.current_user.to_json()
    else:
        return jsonify({'success':False,
                        'error':'Not login'})

#旅游信息分页获取，用例：{'index':1} 请求第一页
@app.route('/c2c/travelmessage/list/',methods=['GET','POST'])
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

#旅游信息页面请求
@app.route('/c2c/travelmessage/<int:tm_id>',methods=['GET'])
def travelmessage_id(tm_id):
    tm = TravelMessage.query.get(tm.id)
    if tm:
        return app.send_satic_file('travelmessage_info.html')
    else:
        return app.send_static_file('404.html')

#旅游信息页面缓加载接口
@app.route('/c2c/travelmessage/show/<int:tm_id>',methods=['GET'])
def travelmessage_id_info(tm_id):
    tm = TravelMessage.query.get(tm.id)
    if tm:
        return tm.to_json()
    else:
        return jsonify({'success':False})

#房源信息分页请求
@app.route('/c2c/accommodation/list/', methods=['GET', 'POST'])
def accommodation():
    print("hello")
    dic = request.get_json()
    if 'index' in dic:
        index = dic['index']
        return_dic = {}
        if isinstance(index, int) and index > 0:
            index = index * 10
            try:
                accommodations = Accommodation.query.all()[index - 10:index - 1]
                for one_acc in accommodations:
                    return_dic[one_acc.acc_id] = {one_acc.acc_description, one_acc.acc_city, one_acc.acc_price}
                return jsonify(return_dic)
            except Exception:
                return jsonify({'success':False,
                                'error':'DB query Failed'})
    else:
        return jsonify({'success': False})

#对应房源信息的图片请求接口
@app.route('/c2c/accommodation/image/<int:acc_id>',methods=['GET'])
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

#对应单个房源信息展示页面请求
@app.route('/c2c/accommodation/<int:acc_id>', methods=['GET'])
def accommodation_id(acc_id):
    one_acc = Accommodation.query.get(acc_id)
    if one_acc:
        return app.send_satic_file('accommodation_info.html')
    else:
        return app.send_static_file('404.html')

#对应单个房源信息缓加载请求
@app.route('/c2c/accommodation/show/<int:acc_id>', methods=['GET'])
def accommodation_id_info(acc_id):
    one_acc = Accommodation.query.get(acc_id)
    if one_acc:
        return one_acc.to_json()
    else:
        return jsonify({'success': False,
                        'error':'DB query Failed'})

#房源信息添加接口
@app.route('/c2c/accommodation/add',methods=['GET','POST'])
def accommodation_add():
    data=request.get_json()
    oneAcc = Accommodation(
        acc_address = data['acc_address'],
        acc_capacity = data['acc_capacity'],
        acc_price = data['acc_price'],
        acc_city = data['acc_city'],
        acc_description = data['acc_description'],
        acc_user_id = data['acc_user_id'],
        acc_type_id = data['acc_type_id'],
        acc_datetype = date['acc_datetype'],
        acc_images = data['acc_images']
    )
    try:
        db.session.add(oneAcc)
        db.session.commit()

        return jsonify({'success':True})
    except Exception:
        return jsonify({'success':False})

#删除单个房源信息接口
@app.route('/c2c/del_one_accommodation/<int:acc_id>',methods=['POST','GET'])
def del_one_accommodation(acc_id):
    oneAcc = Accommodation.query.get(acc_id)
    if(not oneAcc):
        return jsonify({'success':False,
                        'error':'DB query Failed'})

    if (g.current_user.role_id != 2 and oneAcc.acc_user_id != g.current_user.user_id):
        return jsonify({'success':False,
                        'error':'Role Failed'})
    if oneAcc:
        try:
            db.session.delete(oneAcc)
            db.session.commit()
            return jsonify({'success':True})
        except Exception:
            return jsonify({'success':False,
                            'error':'DB remove Failed'})
    else:
        return jsonify({'success':False,
                        'error':'DB query Failed'})



#房源信息更新
@app.route('/c2c/accommodation/update/',methods=['GET','POST'])
def accommodation_update():
    # 判断是否是出租者
    if not g.current_user:
        return jsonify({'success': False})
    if g.current_user.role_id != 3:
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
        oneAcc.acc_description = data['acc_description']
        oneAcc.acc_user_id = data['acc_user_id']
        oneAcc.acc_type_id = data['acc_type_id']
        oneAcc.acc_city = data['acc_city']
        oneAcc.acc_images = data['acc_images']
        try:
            db.session.commit()
        except Exception:
            return jsonify({'success': False})
    else:
        return jsonify({'success': False})    



@app.route('/c2c/reservation/add',methods=['GET','POST'])
def reservation_add():
    data=request.get_json()
    oneRes = Reservation(
        res_id = data['res_id'],
        tenant_id = data['tenant_id'],
        demand = data['demand'],
        acc_id = data['acc_area'],
        state_id= data['state_id '],
        date = data['date'],
    )
    try:
        db.session.add(oneRes)
        db.session.commit()
        return jsonify({'success':True})
    except Exception:
        return jsonify({'success':False})


@app.route('/c2c/accommodation/browse/', methods=['GET', 'POST'])
def browse():
    dic = request.get_json()
    if 'index' in dic:
        index = dic['index']
        return_dic = {}
        if isinstance(index, int) and index > 0:
            index = index * 10
            accommodations = Accommodation.query.eq('acc_city')[index - 10:index - 1]
            for one_acc in accommodations:
                return_dic[one_acc.acc_id] = {one_acc.acc_description, one_acc.acc_address,one_acc.acc_capacity, one_acc.acc_price}
            return jsonify(return_dic)
    else:
        return jsonify({'success': False})


@app.route('/c2c/rolechange',methods=['POST'])
def role_change():
    if g.current_user:
        if g.current_user.role_id == 1:
            data = request.get_json()
            user_id = data['user_id']
            role = data['role']
            if(role>=2):
                user = User.query.get(user_id)
                user.role_id = role 
                db.session.commit()
            else:
                return jsonify({'success':False})
        else: 
                return jsonify({'success':False})
    else:
        return jsonify({'success':False})


@app.route('/c2c/city',methods=['POST','GET'])
def city_info():
    city = City.query.get(1)
    return jsonify({'name':city.city_name})

@app.route('/c2c/upload',methods=['POST','GET'])
def upload():
    if not g.current_user:
        return jsonify({'success':False,
                        'error':'Not login'})
    key = datetime.now().strftime("%Y-%m-%d%H%M%S")+".png"
    token = qiniu_handle.upload_token(bucket_name,key,3600,policy)
    return jsonify({'success':True,
                    'key':key,
                    'domain':bucket_domain,
                    'token':token})

@app.route('/c2c/headico',methods=['POST','GET'])
def headico_upload():
    data = request.get_json()
    if not g.current_user:
        return jsonify({'success':False,
                        'error':'Not login'})
    if 'headico' not in data:
        return jsonify({'success':False, 'error':'No key value'}) 
    try:    
        user = User.query.get(g.current_user.user_id)
        user.headico = data['headico']
        db.session.commit()
        return jsonify({'success':True})
    except:
        return jsonify({'success':False,
                        'error':"DB Error"})
