from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
#import os
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mercado.db'

app.config['SECRET_KEY'] = 'a2410c4c8e9b3875c402d45f'#os.urandom(12).hex()


db.init_app(app)
bcrypt = Bcrypt(app)

from mercado import routes