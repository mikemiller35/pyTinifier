import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    # Full URL
    HOST = os.environ.get('FULL_URL') or "http://localhost:5000/"
    # sqlite3 info. will move to psql
    SQLITE = os.environ.get('DBHOST') or 'urls.db'    