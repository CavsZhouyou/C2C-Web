from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from .models import db
import os 

app=Flask(__name__,static_url_path='')
app.config.from_object('config')

from app import views
