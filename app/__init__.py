from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
app = Flask(__name__) # represents the application itself
app.config.from_object(Config) # represents the configuration of the application
db = SQLAlchemy(app) # represents the database
migrate = Migrate(app, db) # represents the migration engine
login = LoginManager(app) # represents the login manager
login.login_view = 'login'

from app import routes, models
