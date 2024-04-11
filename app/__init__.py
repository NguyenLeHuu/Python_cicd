# app/__init__.py
from flask import Blueprint
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
print('chạy init')

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:070900@localhost/pythont_test?charset=utf8mp4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app = app)

add = Blueprint('add', __name__)
minute = Blueprint('minute', __name__)

