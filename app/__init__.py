from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from .models import db
from qiniu import Auth  
import os 

access_key = 'qHyZn42sB0ZU2X6rYwugx3rgjDnG1SZD-5c01F5y'
secret_key = 'YERUm0zdzKul3mPq-u_8GHzjye98HiD7eeDygpi7'
bucket_name = 'c2cweb'
bucket_domain ='pbn2nc8d5.bkt.clouddn.com' 

qiniu_handle = Auth(access_key,secret_key)
policy={
}

app=Flask(__name__,static_url_path='')
app.config.from_object('config')
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024
db.init_app(app)


from app import views
