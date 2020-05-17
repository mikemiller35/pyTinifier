import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    # Docker?
    DOCKER = os.environ.get('DOCKER') or False
    # Host Info
    HOST = os.environ.get('HOST') or "http://localhost:5000/"
    # HOSTPORT = os.environ.get('HOSTPORT') or '80'
    # sqlite3 info
    SQLITE = os.environ.get('DBHOST') or 'urls.db'    