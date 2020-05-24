import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    # Full URL
    HOST = os.environ.get('FULL_URL') or "http://localhost:5000/"   
    # Database
    DBHOST = os.environ.get('DBHOST') or '127.0.0.1'
    DBPORT = os.environ.get('DBPORT') or '5432'
    DBUSER = os.environ.get('DBUSER') or ''
    DBPASS = os.environ.get('DBPASS') or 'password'
    DBDB = os.environ.get('DBDB') or 'pytinifier'
    # Heroku setup
    DATABASE_URL = os.environ.get('DATABASE_URL')
    # RDS
    RDS_DB_NAME = os.environ.get('RDS_DB_NAME')
    RDS_USERNAME = os.environ.get('RDS_USERNAME')
    RDS_PASSWORD = os.environ.get('RDS_PASSWORD')
    RDS_HOSTNAME = os.environ.get('RDS_HOSTNAME')
    RDS_PORT = os.environ.get('RDS_PORT')
    # Is the DB setup?
    SETUP = os.environ.get('IS_SETUP') or 1
    