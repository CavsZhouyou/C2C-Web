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




