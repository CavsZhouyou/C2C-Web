from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from flask import jsonify
import re
#初始化数据库变量
db = SQLAlchemy()


#通过继承db.Model,可以直接由迁移程序将模型映射到数据库
class User(db.Model):
    user_id = db.Column(db.Integer,autoincrement=True,nullable=False,unique=True,primary_key=True)
    nickname = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100),nullable=False)
    phone = db.Column(db.String(50),nullable=False)
    registerdate = db.Column(db.DateTime,nullable=False,default=datetime.now)
    role_id = db.Column(db.Integer,db.ForeignKey('role.role_id'))
    address = db.Column(db.String(100),nullable=True)
    name = db.Column(db.String(100),nullable=False)
    id_card = db.Column(db.String(100),nullable=False)
    info = db.Column(db.Text,nullable=True)

    def __init__(self,nickname,password,email,phone,role_id,name,id_card):
        self.nickname = nickname 
        self.password = password 
        self.email = email 
        self.phone = phone 
        self.registerdate = datetime.now()
        self.name = name 
        self.id_card = id_card 
        self.info = ""
        if(role_id!=3 and role_id!=4):
            self.role_id = 4
        else:
            self.role_id = role_id

    @staticmethod 
    def usercheck(email,password):
        filter_bytes="\' "
        if len(email)<5 or len(email)>20:
            return False 
        #验证密码长度和空格
        if len(password)<5 or len(password)>50:
            return False 
        #非法字符验证
        for byte in filter_bytes:
            if byte in email or byte in password:
                return False 

        #正则表达式验证邮箱地址格式
        reg_filter = r'(^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$)'
        filter_format = re.compile(reg_filter)
        item = filter_format.findall(email)
        if not item[0]:
            return False 
        filters = {'email':email,'password':password}
        user = User.query.filter_by(**filters).first()
        if user:
            return user 
        else: 
            return False 
    @staticmethod
    def useradd(user):
        #查重
        finduser = User.query.filter_by(email = user.email).first()
        if finduser:
            return False 
        else:
            try:
                db.session.add(user)
                db.session.commit()
                return True
            except Exception:
                return False 

    def to_json(self):
        return jsonify({
                'user_id':self.user_id,
                'nickname':self.nickname,
                'email':self.email,
                'phone':self.phone,
                'address':self.address,
                'info':self.info,
                'success':True
                })
        

#旅行信息推送
class TravelMessage(db.Model):
    __tablename__ = 'travelmessage'
    tmessage_id = db.Column(db.Integer,autoincrement=True,nullable=False,unique=True,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))
    title=db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text)
    date = db.Column(db.DateTime,nullable=False,default=datetime.now)
    addressoftravel=db.Column(db.String(100),nullable=False)
    
    def __init__(self,user_id,title,content,addressoftravel):
        self.user_id = user_id 
        self.title = title 
        self.content = content 
        self.date = datetime.now()
        self.addressoftravel = addressoftravel 

    def to_json(self):
        return jsonify({
            'tmessage_id':self.tmessage_id,
            'user_id':self.user_id,
            'title':self.title,
            'content':self.content,
            'date':self.date,
            'addressoftravel':self.addressoftravel
            })

#免责声明
class Disclaimer(db.Model):
    __tablename__= 'disclaimer'
    disclaimer_id = db.Column(db.Integer,autoincrement=True,nullable=False,unique=True,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))
    content = db.Column(db.Text)
    title = db.Column(db.String(100),nullable=False)
    publishdate = db.Column(db.DateTime,nullable=False,default=datetime.now)
    
    def __init__(self,user_id,title,content):
        self.user_id = user_id 
        self.title = title 
        self.content = content 
        publishdate = datetime.now()

    def to_json(self):
        return jsonify({
            'title':self.title,
            'content':self.title,
            'publishdate:':self.publishdate
            })

#房源类型
class AccommodationType(db.Model):
    __tablename__ = 'accommodationtype'
    acctype_id = db.Column(db.Integer,autoincrement=True,nullable=False,unique=True,primary_key=True)  #类型ID
    acctype_description = db.Column(db.String(255))      #类型描述

    def to_json(self):
        return jsonify({
            'acctype_description':self.acctype_description
            })
#房源
class Accommodation(db.Model):
    __tablename__ = 'accommodation'
    acc_id = db.Column(db.Integer,autoincrement=True,nullable=False,unique=True,primary_key=True)    #房源ID
    acc_address = db.Column(db.String(255))            #房源地址
    acc_capacity = db.Column(db.Integer)               #房源面积
    acc_price = db.Column(db.String(100))                  #房源价格
    acc_datetype = db.Column(db.Integer,db.ForeignKey('datetype.type_id'))
    acc_city = db.Column(db.Integer,db.ForeignKey('city.city_id'))               #房源区域
    acc_description = db.Column(db.String(255))        #房源描述
    acc_user_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))               #拥有者ID
    acc_type_id = db.Column(db.Integer,db.ForeignKey('accommodationtype.acctype_id'))   #类型id
    
    def __init__(self,acc_address,acc_capacity,acc_price,acc_city,acc_description,acc_user_id,acc_type_id,datetype):
        self.acc_address = acc_address
        self.acc_capacity = acc_capacity
        self.acc_price = acc_price
        self.acc_city =  acc_city 
        self.acc_description = acc_description 
        self.acc_user_id = acc_user_id 
        self.acc_type_id = acc_type_id 
        self.acc_datetype = datetype

    def to_json(self):
        return jsonify({
            'acc_address':self.acc_address,
            'acc_capacity':self.acc_capacity,
            'acc_price':self.acc_price,
            'acc_city':self.acc_city,
            'acc_description':self.acc_description,
            'acc_user_id':self.acc_user_id,
            'acc_type_id':self.acc_type_id,
            'acc_datetype':self.acc_datetype 
            })

# 房源图片
class AccommodationImage(db.Model):
    __tablename__='accommodationimage'
    accImage_id = db.Column(db.Integer,autoincrement=True,nullable=False,unique=True,primary_key=True)    # 图片ID
    accImage_acc_id = db.Column(db.Integer,db.ForeignKey('accommodation.acc_id')) # 房源ID
    accImage_url = db.Column(db.String(255))     # 图片url地址

    def __init__(self,accImage_acc_id,accImage_url):
        self.accImage_acc_id = accImage_acc_id 
        self.accImage_url = accImage_url 



#城市
class City(db.Model):
    __tablename__ = 'city'
    city_id = db.Column(db.Integer,autoincrement=True,nullable=False,unique=True,primary_key=True)
    city_name = db.Column(db.String(20),nullable=False)
    city_info = db.Column(db.Text)

    def to_json(self):
        return jsonify({
            'city_name':self.city_name,
            'city_info':self.info
            })
#合同
class Contract(db.Model):
    __tablename__='contract'
    con_id = db.Column(db.Integer,autoincrement=True,nullable=False,unique=True,primary_key=True)      #合同ID
    con_res_id =  db.Column(db.Integer,db.ForeignKey('reservation.res_id'))      #订单ID
    con_tenant_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))      #租房者ID
    con_lessor_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))      #出租者ID
    con_tenant_option = db.Column(db.Boolean,default=False)      #租房者同意
    con_lessor_option = db.Column(db.Boolean,default=False)      #出租者同意
    con_state_id = db.Column(db.Integer,db.ForeignKey('contractstate.constate_id'))      #合同状态ID
    con_disclaimer_id = db.Column(db.Integer,db.ForeignKey('disclaimer.disclaimer_id'))   #免责声明ID

    def __init__(self,con_res_id,con_tenant_id,con_lessor_id,con_tenant_option,con_lessor_option,con_state_id,con_disclaimer_id):
        self.con_res_id = con_res_id 
        self.con_tenant_id = con_tenant_id 
        self.con_lessor_id = con_lessor_id 
        self.con_tenant_option = con_tenant_option 
        self.con_lessor_option = con_lessor_option 
        self.con_state_id = con_state_id 
        self.con_disclaimer_id = con_disclaimer_id 

    def to_json(self):
        return jsonify({
            'con_res_id':self.con_res_id,
            'con_tenant_id':self.con_tenant_id,
            'con_lessor_id':self.con_lessor_id,
            'con_state_id':self.con_state_id,
            'con_disclaimer_id':self.con_disclaimer_id 
            })

#合同状态
class ContractState(db.Model):
    __tablename__ = 'contractstate'
    constate_id=db.Column(db.Integer,autoincrement=True,nullable=False,unique=True,primary_key=True)       #合同状态ID
    constate_name = db.Column(db.String(50),nullable = False)
    constate_description=db.Column(db.Text)        #合同状态描述
    
    def to_json(self):
        return jsonify({
            'constate_name':self.constate_name,
            'constate_description':self.constate_description
            })

class Role(db.Model):
    __tablename__='role'
    role_id = db.Column(db.Integer,autoincrement=True,nullable=False,unique=True,primary_key=True)
    role_name = db.Column(db.String(50),nullable=False)

    def to_json(self):
        return jsonify({
            'role_name':self.role_name,
            })

#预定信息表
class Reservation(db.Model):
    __tablename__ = 'reservation'
    res_id = db.Column(db.Integer,autoincrement=True,nullable=False,unique=True,primary_key=True)
    tenant_id = db.Column(db.Integer(),  nullable=False)   #租房者
    demand = db.Column(db.Text, nullable=True)              #备注信息
    acc_id = db.Column(db.Integer,db.ForeignKey('accommodation.acc_id'))
    state_id = db.Column(db.Integer,db.ForeignKey('resstate.state_id'))
    date = db.Column(db.DateTime, nullable=False,default = datetime.now)
    
    def __init__(self,tenant_id,demand,acc_id,state_id):
        self.tenant_id = tenant_id 
        self.demand = demand 
        self.acc_id = acc_id 
        self.state_id = state_id 
        self.date = datetime.now 

    def to_json(self):
        return jsonify({
            'tenant_id':self.tenant_id,
            'demand':self.demand,
            'acc_id':self.acc_id,
            'state_id':self.state_id,
            'date':self.date
            })

#预订信息表状态
class ResState(db.Model):
    __tablename__ = 'resstate'
    state_id = db.Column(db.Integer,autoincrement=True,nullable=False,unique=True,primary_key=True)
    state_name = db.Column(db.String(50),nullable=False)
    state_info = db.Column(db.Text,nullable=True)

    def to_json(self):
        return jsonify({
            'state_name':self.state_name,
            'state_info':self.state_info
            })
 
#评价表
class Comment(db.Model):
    __tablename__='comment'
    comment_id = db.Column(db.Integer,autoincrement=True,nullable=False,unique=True,primary_key=True) 
    from_who= db.Column(db.Integer,db.ForeignKey('user.user_id'))
    to_which = db.Column(db.Integer,db.ForeignKey('reservation.res_id'))
    to_who = db.Column(db.Integer,db.ForeignKey('user.user_id'))
    content = db.Column(db.String(15), nullable=False)
    date = db.Column(db.DateTime, nullable=False,default = datetime.now)

    def __init__(self,from_who,to_which,to_who,content):
        self.from_who = from_who 
        self.to_which = to_which 
        self.to_who = to_who 
        self.content = content 

    def to_json(self):
        return jsonify({
            'from_who':self.from_who,
            'to_which':self.to_which,
            'to_who':self.to_who,
            'content':self.content,
            'date':self.date
            })

#房源信息计费时间单位
class DateType(db.Model):
    __tablename__ = 'datetype'
    type_id = db.Column(db.Integer,autoincrement=True,nullable=False,unique=True,primary_key=True)
    type_name = db.Column(db.String(20),nullable=False)

#县级单位
class County(db.Model):
    __tablename__ = 'county'
    county_id = db.Column(db.Integer,autoincrement=True,nullable=False,unique=True,primary_key=True)
    county_name = db.Column(db.String(20),nullable=False)
    city_id = db.Column(db.Integer,db.ForeignKey("city.city_id"))

class Street(db.Model):
    __tablename__ = 'street'
    street_id = db.Column(db.Integer,autoincrement=True,nullable=False,unique=True,primary_key=True)
    street_name = db.Column(db.String(50),nullable=False)
    county_id = db.Column(db.Integer,db.ForeignKey("county.county_id"))

#用户头像
class UserHeadIco(db.Model):
    __tablename__="userheadico"
    headico_id = db.Column(db.Integer,autoincrement=True,nullable=False,unique=True,primary_key=True)
    headico_name = db.Column(db.String(100),nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))

    
