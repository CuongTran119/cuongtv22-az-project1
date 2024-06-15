"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)
# TODO: Add any logging levels and handlers with app.logger
app.logger.setLevel(logging.CRITICAL)
streamHandler=logging.StreamHandler()
streamHandler.setLevel(logging.CRITICAL)
streamHandler.setLevel(logging.WARNING)
streamHandler.setLevel(logging.ERROR)
app.logger.addHandler(streamHandler)
app.logger.error('Error Sucessfully Logged')
app.logger.warning('Warning Sucessfully Logged')
app.logger.critical('Critical Sucessfully Logged')
# TODO: Add any logging levels and handlers with app.logger
Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
