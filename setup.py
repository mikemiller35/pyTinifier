import psycopg2
import time
from urllib.parse import urlparse

from app import app

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

time.sleep(5)
conn0 = psycopg2.connect(host=host, port=port, database=database,
                         user=user, password=password)


def db_setup():
    time.sleep(3)
    tbl_setup()


def tbl_setup():
    sql = """
        CREATE TABLE IF NOT EXISTS tiny(
   id SERIAL PRIMARY KEY,
   url VARCHAR NOT NULL
    );
    """
    app.logger.info("Creating table if it's not here...")
    app.logger.info(sql)
    conn = psycopg2.connect(host=host, port=port, database=database,
                            user=user, password=password)
    cur = conn.cursor()

    cur.execute(sql)
    cur.close()

    conn.commit()

    app.logger.info('Database setup!')
