from app import app 
from flask import request
from .models import *
import re 
@app.route('/')
def index():
    return "HelloWorld"

@app.route('/login',method['POST'])
    def login():
        email = request.form.get('email','')
        #验证账号长度和空格
        if len(email)<5 or len(email)>20 or ' ' in email:
            return "{success:false}"
        password = request.form.get('password','')
        #验证密码长度和空格
        if len(password)<5 or len(password)>50 or ' ' in email:
            return "{success:false}"
        #正则表达式验证邮箱地址格式
        reg_filter = r'(^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$)'
        filter_format = re.compile(reg_filter)
        item = filter_format.findall(email)
        if not item[0]:
            return "{success:false}"
        user = User.query.filter_by(email=email and password=password).first()
        if user:
            session['user'] = user.user_id
            return "{success:true}"
        else 
            return "{success:false}"
