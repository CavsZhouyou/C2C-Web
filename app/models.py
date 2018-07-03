from flask_sqlalchemy import SQLAlchemy 
#初始化数据库变量
db = SQLAlchemy()


#通过继承db.Model,可以直接由迁移程序将模型映射到数据库
class User(db.Model):
    user_id = db.Column(db.Integer,primary_key=True)



