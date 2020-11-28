import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from config import SecretId, SecretKey

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@127.0.0.1/sign"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = '8906ced739ec4d3a80c0bcecfb15fb8c'
app.config['UPLOADED_PATH'] = os.path.join(os.path.abspath(os.path.dirname(__file__)),"static/uploads/")
app.config['TENCENT_SECRET_ID'] = SecretId
app.config['TENCENT_SECRET_KEY'] = SecretKey
app.debug = True

db = SQLAlchemy(app)

from app.client import client as client_blueprint

app.register_blueprint(client_blueprint)