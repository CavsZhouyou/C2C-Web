from flask_sqlalchemy import SQLAlchemy 
from flask import jsonify
#初始化数据库变量
db = SQLAlchemy()


#通过继承db.Model,可以直接由迁移程序将模型映射到数据库
class User(db.Model):
    user_id = db.Column(db.Integer,primary_key=True)
    
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
        user = User.query.filter(**filters).first()
        if user:
            return user 
        else 
            return False 
    @staticmethod
    def useradd(user):
        #查重
        filters = {'email':user.email}
        finduser = User.query.filter(**filters).first()
        if finduser:
            return False 
        else:
            db.session.add(user)
            db.session.commit()
            return True 
    def getuserinfo(self):
        return jsonify({
                'id':self.user_id,
                'nickname':self.nickname,
                'email':self.email,
                'phone':self.phone,
                'address':self.acc_address
                })
        

#旅行信息推送
class TravelMessage(db.Model):
    __tablename__ = 'travelmessage'
    tmessage_id = db.Column(db.Integer,auto_increment=True,nullable=False,unique=True,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))
    title=db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text)
    date = db.Column(db.DateTime,nullable=False,default=datetime.now))
    addressoftravel=db.Column(db.String(100),nullable=False)
    
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
    disclaimer_id = db.Column(db.Integer,auto_increment=True,nullable=False,unique=True,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))
    content = db.Column(db.Text)
    title = db.Column(db.String(100),nullable=False)
    publishdate = db.Column(db.Datetime,nullable,default=datetime.now)


#房源
class Accommodation(db.Model):
    acc_id = db.Column(db.Integer,auto_increment=True,nullable=False,unique=True,primary_key=True)    #房源ID
    acc_address = db.Column(db.String(255))            #房源地址
    acc_capacity = db.Column(db.Integer)               #房源面积
    acc_price = db.Column(db.Numeric)                  #房源价格
    acc_area = db.Column(db.String(255))               #房源区域
    acc_description = db.Column(db.String(255))        #房源描述
    acc_user_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))               #拥有者ID
    acc_type_id = db.Column(db.Integer,db.ForeignKey('accommodationtype.acctype_id'))   #类型id

#房源类型
class AccommodationType(db.Model):
    acctype_id = db.Column(db.Integer,auto_increment=True,nullable=False,unique=True,primary_key=True)  #类型ID
    acctype_description = db.Column(db.String(255))      #类型描述

#合同
class Contract(db.Model):
    con_id = db.Column(db.Integer,auto_increment=True,nullable=False,unique=True,primary_key=True)      #合同ID
    con_res_id =  db.Column(db.Integer,db.ForeignKey('reservation.res_id'))      #订单ID
    con_res = db.relationship('reservation',backref=db.backref('contract'))
    con_tenant_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))      #租房者ID
    con_tenant = db.relationship('user',backref=db.backref('contract'))
    con_lessor_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))      #出租者ID
    con_lessor = db.relationship('user',backref=db.backref('contract'))
    con_tenant_option = db.Column(db.Boolean,default=False)      #租房者同意
    con_lessor_option = db.Column(db.Boolean,default=False)      #出租者同意
    con_state_id = db.Column(db.Integer,db.ForeignKey('constate.state_id'))      #合同状态ID
    con_disclaimer_id = db.Column(db.Integer,db.ForeignKey('disclaimer.disclaimer_id'))   #免责声明ID

#合同状态
class ContractState(db.model):
    constate_id=db.Column(db.Integer,auto_increment=True,nullable=False,unique=True,primary_key=True)       #合同状态ID
    constate_description=db.Column(db.String)        #合同状态描述
    


