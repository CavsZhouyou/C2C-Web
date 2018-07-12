from app import app,qiniu_handle,bucket_name,policy,bucket_domain
from datetime import datetime
import time 
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
        g.current_user = User.query.get(session['user'])    
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
                            'role_id':user.role_id,
                            'headico':user.headico,
                            'nickname':user.nickname})
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
            user.headico = data['headico']
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

@app.route('/c2c/system/userpasswordchange',methods=['POST','GET'])
def systempassword():
    if not g.current_user:
        return jsonify({'success':False,
                        'error':'Not login'})
    if g.current_user.role_id != 1: 
        return jsonify({'success':False,
                        'error':'No permission'})
    data = request.get_json()
    user_id = data['user_id']
    password = data['password']

    user = User.query.get(user_id)
    user.password = password 
    db.session.commit()
    return jsonify({'success':True})


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
@app.route('/c2c/accommodation/list', methods=['GET', 'POST'])
def accommodation():
    data = request.get_json()
    index = data['index']
    count = data['count']
    if not g.current_user:
        return jsonify({'success':False,
                        'error':'Not login'})
    accommodations = g.current_user.accommodations
    tmp = []
    if((index+count)<len(accommodations)):
        for acc in accommodations[index:index+count]:
            tmp.append({'acc_address':acc.acc_address,
            'acc_id':acc.acc_id,
            'acc_capacity':acc.acc_capacity,
            'acc_price':acc.acc_price,
            'acc_city':acc.city.city_name,
            'acc_description':acc.acc_description,
            'acc_user_id':acc.acc_user_id,
            'acc_type_id':acc.acc_type_id,
            'acc_type_name':acc.acc_type.acctype_description,
            'acc_datetype':acc.acc_datetype,
            'acc_images':acc.acc_images.split(" ")[0],
            'acc_id':acc.acc_id,
            'acc_street':acc.street.street_name,
            'acc_county':acc.county.county_name} 
)
        return jsonify({'success':True,
                        'empty':False,
                        'list':tmp})
    else:
        if(index>len(accommodations)):
            return jsonify({'success':False,
                            'error':"index beyond limit"})
        else:
            for acc in accommodations[index:]:
                tmp.append({'acc_address':acc.acc_address,
                                        'acc_capacity':acc.acc_capacity,
                                        'acc_price':acc.acc_price,
                                        'acc_city':acc.city.city_name,
                                        'acc_description':acc.acc_description,
                                        'acc_user_id':acc.acc_user_id,
                                        'acc_type_id':acc.acc_type.acctype_description,
                                        'acc_type_name':acc.acc_type.acctype_description,
                                        'acc_datetype':acc.acc_datetype,
                                        'acc_images':acc.acc_images.split(" ")[0],
                                        'acc_id':acc.acc_id,
                                        'acc_street':acc.street.street_name,
                                        'acc_county':acc.county.county_name} )
            return jsonify({'success':True,
                            'empty':True,
                            'list':tmp})





#对应单个房源信息缓加载请求
@app.route('/c2c/accommodation/show', methods=['GET','POST'])
def accommodation_id_info():
    data = request.get_json()
    acc_id = data['acc_id']
    one_acc = Accommodation.query.get(acc_id)
    if one_acc:
        return one_acc.to_json()
    else:
        return jsonify({'success': False,
                        'error':'DB query Failed'})


#房源信息添加接口
@app.route('/c2c/accommodation/add',methods=['GET','POST'])
def accommodation_add():
    if not g.current_user:
        return jsonify({'success':False,
                        'error':"Not login"})
    if g.current_user.role_id != 3:
        return jsonify({'success':False,
                        'error':'No permission'})
    data=request.get_json()
    oneAcc = Accommodation(
        acc_address = data['acc_address'],
        acc_capacity = data['acc_capacity'],
        acc_price = data['acc_price'],
        acc_city = data['acc_city'],
        acc_description = data['acc_description'],
        acc_user_id = g.current_user.user_id,
        acc_type_id = data['acc_type_id'],
        acc_datetype = data['acc_datetype'],
        acc_images = data['acc_images'],
        acc_county = data['acc_county'],
        acc_street = data['acc_street']
    )
    try:
        db.session.add(oneAcc)
        db.session.commit()

        return jsonify({'success':True})
    except Exception:
        return jsonify({'success':False})


#删除单个房源信息接口
@app.route('/c2c/accommodation/delete',methods=['POST','GET'])
def del_one_accommodation():
    if not g.current_user:
        return jsonify({'success':False,
                        'error':'Not login'})
    data = request.get_json()
    
    oneAcc = Accommodation.query.get(data['acc_id'])
    if(not oneAcc):
        return jsonify({'success':False,
                        'error':'DB query Failed'})
    if oneAcc.acc_user_id != g.current_user.user_id:
        return jsonify({'success':False,
                        'error':'No permission'})

    reservations = oneAcc.reservations

    for reservation in reservations:
        if(reservation.state_id == 2):
            return jsonify({'success':False,
                            'error':"该房源有订单正在生效"})
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
@app.route('/c2c/accommodation/update',methods=['GET','POST'])
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
            return jsonify({'success': False,
                    'error':'No permission'})
    else:
        return jsonify({'success': False,
                        'error':'No acc id'})

    #修改房源
    if oneAcc:
        try:
            oneAcc.acc_address = data['acc_address']
            oneAcc.acc_capacity = data['acc_capacity']
            oneAcc.acc_price = data['acc_price']
            oneAcc.acc_description = data['acc_description']
            oneAcc.acc_user_id = data['acc_user_id']
            oneAcc.acc_type_id = data['acc_type_id']
            oneAcc.acc_city = data['acc_city']
            oneAcc.acc_street=data['acc_street']
            oneAcc.acc_county=data['acc_county']
            oneAcc.acc_images = data['acc_images']
            db.session.commit()
            return jsonify({'success':True})
        except Exception:
            return jsonify({'success': False,
                            'error':'DB Error'})
    else:
        return jsonify({'success': False})    


@app.route('/c2c/reservation/request',methods=['POST','GET'])
def reservation_request():
    data = request.get_json()
    if not g.current_user:
        return jsonify({'success':False,
                        'error':"Not login"})
    if g.current_user.role_id !=4:
        return jsonify({'success':False,
                        'error':"No permission"})
    acc_id = data['acc_id']
    acc = Accommodation.query.get(acc_id)
    
    return jsonify({'success':True,
                    'lessor_name':acc.user.name,
                    'lessor_id_card':acc.user.id_card,
                    'tenant_name':g.current_user.name,
                    'tenant_id_card':g.current_user.id_card,
                    'acc_type':acc.acc_type_id,
                    'acc_capacity':acc.acc_capacity,
                    'acc_address':acc.city.city_name+' '+acc.county.county_name+' '+acc.street.street_name+' '+ acc.acc_address,
                    'price':acc.acc_price 
                    })

@app.route('/c2c/reservation/add',methods=['GET','POST'])
def reservation_add():
    if not g.current_user:
        return jsonify({'success':False,
                        'error':'未登录'})
    if g.current_user.role_id !=4:
        return jsonif({'success':False,
                        'error':'No permission'})
    data=request.get_json()
    oneAcc = Accommodation.query.get(data['acc_id'])
    oneRes = Reservation(
        tenant_id = g.current_user.user_id,
        demand = data['demand'],
        acc_id = data['acc_id'],
        res_price=data['price'],
        state_id= 1,
        begin = data['begin']/1000,
        end = data['end']/1000,
        acc_user_id = oneAcc.acc_user_id 
    )
    try:
        db.session.add(oneRes)
        db.session.commit()
        return jsonify({'success':True})
    except Exception:
        return jsonify({'success':False})

@app.route('/c2c/reservation/list',methods=['POST','GET'])
def reservation_lessor_list():
    if not g.current_user:
        return jsonify({'success':False,
                        'error':"Not login"})
    data = request.get_json()
    index = data['index']
    count = data['count']

    reservations=[]

    if(g.current_user.role_id==4):
        reservations = Reservation.query.filter(Reservation.tenant_id == g.current_user.user_id).order_by(Reservation.state_id).all()
    elif g.current_user.role_id==3: 
        reservations = Reservation.query.filter(Reservation.acc_user_id == g.current_user.user_id).order_by(Reservation.state_id).all()
    elif g.current_user.role_id==2:
        reservations = Reservation.query.all()
    else:
        return jsonify({'success':False})

    tmp=[]

    if((index+count)<len(reservations)):
        for reservation in reservations[index:index+count]:
            tmp.append({'tenant_name':reservation.tenant.name,
                    'tenant_phone':reservation.tenant.phone,
                    'lessor_name':reservation.accommodation.user.name,
                    'lessor_phone':reservation.accommodation.user.phone,
                    'price':reservation.res_price,
                    'reservation_id':reservation.res_id,
                    'acc_id':reservation.acc_id,
                    'state_id':reservation.state_id,
                    'state_name':reservation.state.state_name,
                    'date':time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(reservation.begin))+'-'+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(reservation.end))
                    })
        return jsonify({'success':True,
                        'empty':False,
                        'reservations':tmp})
    else:
        if(index>len(reservations)):
            return jsonify({'success':False,
                            'error':"index beyond limit"})
        else:
            for reservation in reservations[index:]:
                tmp.append({'tenant_name':reservation.tenant.name,
                        'tenant_phone':reservation.tenant.phone,
                        'lessor_name':reservation.accommodation.user.name,
                        'lessor_phone':reservation.accommodation.user.phone,
                        'price':reservation.res_price,
                        'reservation_id':reservation.res_id,
                        'acc_id':reservation.acc_id,
                        'state_id':reservation.state_id,
                        'state_name':reservation.state.state_name,
                        'date':datetime.utcfromtimestamp(reservation.begin).strftime("%Y-%m-%d")+'-'+datetime.utcfromtimestamp(reservation.end).strftime("%Y-%m-%d"),
                        'image':reservation.accommodation.acc_images.split(" ")[0]
                        })
            return jsonify({'success':True,
                        'empty':True,
                        'reservations':tmp})



@app.route('/c2c/rolechange',methods=['POST'])
def role_change():
    if g.current_user:
        if g.current_user.role_id == 1:
            data = request.get_json()
            user_id = data['user_id']
            user = User.query.get(user_id)
            if(user.role_id>=2):
                user.role_id = 2
                db.session.commit()
                return jsonify({'success':True})
            else:
                return jsonify({'success':False})
        else: 
                return jsonify({'success':False})
    else:
        return jsonify({'success':False})

@app.route('/c2c/userdel',methods=['POST','GET'])
def userdel():
    if g.current_user:
        if g.current_user.role_id == 1:
            data = request.get_json()
            user_id = data['user_id']
            user = User.query.get(user_id)
            if(user.role_id>=2):
                db.session.delete(user)
                db.session.commit()
                return jsonify({'success':True})
            else:
                return jsonify({'success':False})
        else:
            return jsonify({'success':False,
                            'error':'No permission'})
    else:
        return jsonify({'success':False,
                        'error':'Not login'})

@app.route('/c2c/city',methods=['POST','GET'])
def city_info():
    citys = City.query.all()
    city_list = []
    for city in citys:
        city_list.append({'label':city.city_name,'value':city.city_id,})
    return jsonify({'success':True,
                    'citys':city_list})

@app.route('/c2c/county',methods=['POST','GET'])
def county_info():
    data = request.get_json()
    city_id = data['city_id']
    city = City.query.get(city_id)
    counties = city.counties
    county_list=[]
    for county in counties:
        county_list.append({'label':county.county_name,'value':county.county_id})
    return jsonify({'success':True,
                    'counties':county_list})

@app.route('/c2c/street',methods=['POST','GET'])
def street_info():
    data = request.get_json()
    county_id = data['county_id']
    county = County.query.get(county_id)
    streets = county.streets 
    street_list=[]
    for street in streets:
        street_list.append({'label':street.street_name,'value':street.street_id})
    return jsonify({'success':True,
                    'streets':street_list})

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

@app.route('/c2c/userlist',methods=['POST','GET'])
def userlist():
    data = request.get_json()
    index = data['index']
    count = data['count']

    if not g.current_user:
        return jsonify({'success':False,
                        'error':'Not login'})
    if g.current_user.role_id != 1:
        return jsonify({'success':False,
                        'error':"No permission"})

    users = User.query.filter(User.role_id != 1).all()
    tmp=[]

    if((index+count)<len(users)):
        for user in users[index:index+count]:
            tmp.append({'user_id':user.user_id,
                        'nickname':user.nickname,
                        'role_id':user.role_id,
                        'role_name':user.role.role_name,
                        'phone':user.phone,
                        'email':user.email,
                        'name':user.name,
                        'id_card':user.id_card,
                        'headico':user.headico 
                        })
        return jsonify({'success':True,
                        'empty':False,
                        'users':tmp})
    else:
        if(index>len(users)):
            return jsonify({'success':False,
                            'error':"index beyond limit"})
        else:
            for user in users[index:]:
                tmp.append({'user_id':user.user_id,
                        'nickname':user.nickname,
                        'role_id':user.role_id,
                        'role_name':user.role.role_name,
                        'phone':user.phone,
                        'email':user.email,
                        'headico':user.headico,
                        'name':user.name,
                        'id_card':user.id_card
                        })
            return jsonify({'success':True,
                        'empty':True,
                        'users':tmp})


@app.route('/c2c/filter',methods = ['POST','GET'])
def acc_filter():
    data = request.get_json()
    city_id = data['city_id']
    county_id = data['county_id']
    street_id = data['street_id']
    start = data['start']
    end = data['end']
    min_price = data['min_price']
    max_price = data['max_price']
    min_capacity = data['min_capacity']
    max_capacity = data['max_capacity']
    acc_type = data['acc_type']
    index = data['index']
    count = data['count']

    if max_price == 0:
        max_price = 100000000
    if max_capacity == 0: 
        max_capacity = 100000000

    filter_list = {
            Accommodation.acc_price > min_price,
            Accommodation.acc_price <= max_price,
            Accommodation.acc_capacity > min_capacity,
            Accommodation.acc_capacity <= max_capacity
            }

    if(city_id!=0):
        filter_list.add(Accommodation.acc_city == city_id)

    if(county_id!=0):
        filter_list.add(Accommodation.acc_county == county_id)

    if(street_id !=0):
        filter_list.add(Accommodation.acc_street == street_id) 

    if(acc_type!=0):
        filter_list.add(Accommodation.acc_type_id == acc_type)

    accommodations = Accommodation.query.filter(*filter_list).all()

    if(start!=None and end != None):
        for acc in accommodations:
            for res in acc.reservations:
                if not (end < res.start or start> res.end):
                    accommodations.pop(acc)
                    break
    tmp = []
         
    if((index+count)<len(accommodations)):
        for acc in accommodations[index:index+count]:
            tmp.append({'acc_id':acc.acc_id,
                        'headico':acc.user.headico,
                        'acc_price':acc.acc_price,
                        'acc_capacity':acc.acc_capacity,
                        'acc_address':acc.acc_address,
                        'acc_images':acc.acc_images.split(" "),
                        'acc_type':acc.acc_type.acctype_description,
                        'acc_comment':Comment.query.filter(Comment.to_who==acc.acc_user_id).count()
                        })
        return jsonify({'success':True,
                        'empty':False,
                        'accommodations':tmp})
    else:
        if(index>len(accommodations)):
            return jsonify({'success':False,
                            'error':"index beyond limit"})
        else:
            for acc in accommodations[index:]:
                tmp.append({'acc_id':acc.acc_id,
                        'headico':acc.user.headico,
                        'acc_price':acc.acc_price,
                        'acc_capacity':acc.acc_capacity,
                        'acc_address':acc.acc_address,
                        'acc_images':acc.acc_images.split(" "),
                        'acc_type':acc.acc_type.acctype_description,
                        'acc_comment':Comment.query.filter(Comment.to_who==acc.acc_user_id).count()
                        })
            return jsonify({'success':True,
                        'empty':True,
                        'accommodations':tmp})
    

@app.route('/c2c/comment/list',methods=['POST','GET'])
def commentlist():
    data = request.get_json()
    index = data['index']
    count = data['count']
    oneAcc = Accommodation.query.get(data['acc_id'])
    comments = Comment.query.filter(Comment.to_who==oneAcc.acc_user_id).order_by(Comment.date.desc()).all()
    tmp=[]

    if((index+count)<len(comments)):
        for comment in comments[index:index+count]:
            user = User.query.get(comment.from_who)
            tmp.append({'headico':user.headico,
                    'nickname':user.nickname,
                    'content':comment.content,
                    'date':comment.date.strftime("%Y-%m-%d %H:%M:%S")
                    })
        return jsonify({'success':True,
                        'empty':False,
                        'comments':tmp})
    else:
        if(index>len(comments)):
            return jsonify({'success':False,
                            'error':"index beyond limit"})
        else:
            for comment in comments[index:]:
                user = User.query.get(comment.from_who)
                tmp.append({'headico':user.headico,
                        'nickname':user.nickname,
                        'content':comment.content,
                        'date':comment.date.strftime("%Y-%m-%d %H:%M:%S")
                        })
            return jsonify({'success':True,
                        'empty':True,
                        'comments':tmp})

#订单取消
@app.route('/c2c/reservation/delete',methods = ['POST','GET'])
def reservation_delete():
    if not g.current_user:
        return jsonify({'success':False,
                        'error':'No login'})
    data = request.get_json()
    reservation = Reservation.query.get(data['res_id'])
    if reservation.tenant_id != g.current_user.user_id and g.current_user.role_id!=2:
        return jsonify({"success":False,
                        "error":"No permission"})
    if g.current_user.role_id == 2:
        db.session.delete(reservation)
        db.session.commit()
        return jsonify({'success':True})

    if reservation.state_id == 3:
        return jsonify({'success':False,
                        'error':'订单已完成，不可删除'})
    elif reservation.state_id ==1:
        db.session.delete(reservation)
        db.session.commit()
        return jsonify({'success':True})
    elif reservation.state_id ==2:
        comment = Comment(g.current_user.user_id,reservation.accommodation.acc_user_id,data['content'])
        #添加评论
        db.session.add(comment)
        reservation.state_id=3 
        db.session.commit()
        return jsonify({'success':True})
    else:
        return jsonify({'success':False})


#订单接受或者拒绝
@app.route('/c2c/reservation/accept',methods =['POST','GET'])
def reservation_accept():
    if not g.current_user:
        return jsonify({'success':False,
                        'error':'Not login'})
    if g.current_user.role_id!=3:
        return jsonify({'success':False,
                'error':'No permission'})
    data = request.get_json()
    reservation = Reservation.query.get(data['res_id'])
    if reservation.accommodation.acc_user_id != g.current_user.user_id:
        return jsonify({'success':False,
                        'error':'No permission'})

    if reservation.state_id == 1:
        if(data['accept']):
            reservation.state_id = 2
            db.session.commit()
        else:
            db.session.delete(reservation)
            db.session.commit()
        return jsonify({'success':True})
    else:
        return jsonify({'success':False,
                        'error':'No permission'})

