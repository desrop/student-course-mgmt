import os
from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SECRET_KEY'] = '712a59c234ec4b9c54e0f09277d83e13'
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://postgres:{os.environ.get('DB_CONNECT')}@studentmgmt-db:5432/studentmgmt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

from studentmgmt import route