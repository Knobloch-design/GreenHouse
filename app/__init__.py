from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "scecret-key-goes-here"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///SproutSmartpython     .db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
from app import routes

# The login_manager object from the flask_login extension is then created, and its init_app() method is passed the app variable.
