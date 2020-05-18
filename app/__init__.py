from flask import Flask
from config import Config
import logging, os
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

app.config.from_object(Config)

if not os.path.exists('logs'):
    os.mkdir('logs')

# Normal logging setup
file_handler = RotatingFileHandler('logs/tinifier.log', maxBytes=10240, backupCount=10)
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

import setup

setup.dbCheck()
setup.dbSetup()
app.logger.info('Done with setup')

from app import routes, errors, edCoder