import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    # Full URL
    HOST = os.environ.get('FULL_URL') or "http://localhost:5000/"
    # sqlite3 info. will move to psql
    SQLITE = os.environ.get('DBHOST') or 'urls.db'   
    # Database
    DBHOST = os.environ.get('DBHOST') or '127.0.0.1'
    DBPORT = os.environ.get('DBPORT') or '5432'
    DBUSER = os.environ.get('DBUSER') or ''
    DBPASS = os.environ.get('DBPASS') or 'password'
    DBDB = os.environ.get('DBDB') or 'pytinifier'
    DATABASE_URL = os.environ.get('DATABASE_URL')