from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from .models import db

app=Flask(__name__)
app.config.from_object('config')

from app import views
