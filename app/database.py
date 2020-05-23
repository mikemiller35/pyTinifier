from urllib.parse import urlparse
import psycopg2
from app import app

con = cur = db = None


def connect():
    global con, cur, db
    if app.config['DATABASE_URL'] is None or app.config['DATABASE_URL'] == '':
        if app.config['RDS_HOSTNAME'] is None or app.config['RDS_HOSTNAME'] == '':
            host = app.config['DBHOST']
            port = app.config['DBPORT']
            database = app.config['DBDB']
            user = app.config['DBUSER']
            password = app.config['DBPASS']
        else: 
            host = app.config['RDS_HOSTNAME']
            port = app.config['RDS_PORT']
            database = app.config['RDS_DB_NAME']
            user = app.config['RDS_USERNAME']
            password = app.config['RDS_PASSWORD']
    else:
        uri = urlparse(app.config['DATABASE_URL'])
        host = uri.hostname
        port = '5432'
        database = uri.path[1:]
        user = uri.username
        password = uri.password
    try:
        con = psycopg2.connect(host=host, port=port, database=database,
                               user=user, password=password)
        cur = con.cursor()
        db = cur.execute
    except psycopg2.DatabaseError as err:
        if con:
            con.rollback()
        print(err)


def init_db_conn():
    if not (con and cur and db):
        connect()
    return con, cur, db
