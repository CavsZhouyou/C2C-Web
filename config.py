#数据库连接地址
SQLALCHEMY_DATABASE_URI = "mysql://flask:1611102@localhost/c2cweb?unix_socket=/opt/zbox/tmp/mysql/mysql.sock"
#如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存
SQLALCHEMY_TRACK_MODIFICATIONS=True
