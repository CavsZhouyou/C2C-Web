from flask_sqlalchemy import SQLAlchemy 
#初始化数据库变量
db = SQLAlchemy()


#通过继承db.Model,可以直接由迁移程序将模型映射到数据库
class User(db.Model):
    user_id = db.Column(db.Integer,primary_key=True)

#旅行信息推送
class TravelMessage(db.Model):
    __tablename__ = 'travelmessage'
    tmessage_id = db.Column(db.Integer,auto_increment=True,nullable=False,unique=True,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))
    title=db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text)
    date = db.Column(db.DateTime,nullable=False,default=datetime.now))
    addressOftravel=db.Column(db.String(100),nullable=False)

#免责声明
class Disclaimer(db.Model):
    __tablename__= 'disclaimer'
    disclaimer_id = db.Column(db.Integer,auto_increment=True,nullable=False,unique=True,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))
    content = db.Column(db.Text)
    title = db.Column(db.String(100),nullable=False)
    publishdate = db.Column(db.Datetime,nullable,default=datetime.now)


#房源
class Accommodation(db.Model):
    acc_id = db.Colum(db.Integer,primary_key=True)    #房源ID
    acc_address = db.Colum(db.String(255))            #房源地址
    acc_capacity = db.Colum(db.Integer)               #房源面积
    acc_price = db.Colum(db.Numeric)                  #房源价格
    acc_area = db.Colum(db.String(255))               #房源区域
    acc_description = db.Colum(db.String(255))        #房源描述
    acc_user_id = db.Colum(db.Integer,db.ForeignKey('user.user_id'))               #拥有者ID
    acc_owner = db.relationship('user',backref=db.backref('accommodation'))
    acc_type_id = db.Colum(db.Integer,db.ForeignKey('accommodationtype.acctype_id'))   #类型id
    acc_type = db.relationship('accommodationtype',backref=db.backref('accommodation'))

#房源类型
class AccommodationType(db.Model):
    acctype_id = db.Colum(db.Integer,primary_key=True)  #类型ID
    acctype_description = db.Colum(db.String(255))      #类型描述

#合同
class Contract(db.Model):
    con_id = db.Colum(db.Integer,primary_key=True)      #合同ID
    con_res_id =  db.Colum(db.Integer,db.ForeignKey('reservation.res_id'))      #订单ID
    con_res = db.relationship('reservation',backref=db.backref('contract'))
    con_tenant_id = db.Colum(db.Integer,db.ForeignKey('user.user_id'))      #租房者ID
    con_tenant = db.relationship('user',backref=db.backref('contract'))
    con_lessor_id = db.Colum(db.Integer,db.ForeignKey('user.user_id'))      #出租者ID
    con_lessor = db.relationship('user',backref=db.backref('contract'))
    con_tenant_option = db.Colum(db.Boolean,default=False)      #租房者同意
    con_lessor_option = db.Colum(db.Boolean,default=False)      #出租者同意
    con_state_id = db.Colum(db.Integer,db.ForeignKey('constate.state_id'))      #合同状态ID
    con_state = db.relationship('contractstate',backref=db.backref('contract'))
    con_disclaimer_id = db.Colum(db.Integer,db.ForeignKey('disclaimer.disclaimer_id'))   #免责声明ID
    con_disclaimer = db.relationship('disclaimer',backref=db.backref('contract'))

#合同状态
class ContractState(db.model):
    constate_id=db.Colum(db.Integer,primary_key=True)       #合同状态ID
    constate_description=db.Colum(db.String)        #合同状态描述
    


