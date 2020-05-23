from app import app
import time, psycopg2
from random import randrange
from urllib.parse import urlparse
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

if app.config['DATABASE_URL'] is None or app.config['DATABASE_URL'] == '':
    host = app.config['DBHOST']
    port = app.config['DBPORT']
    database = app.config['DBDB']
    user = app.config['DBUSER']
    password = app.config['DBPASS']
else:
    uri = urlparse(app.config['DATABASE_URL'])
    host = uri.hostname
    port = '5432'
    database = uri.path[1:]
    user = uri.username
    password = uri.password

conn0 = psycopg2.connect(host=host, port=port, database=database,
                                        user=user, password=password)


def dbSetup():
    conn0.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn0.cursor()
    sql = """
    SELECT 'CREATE DATABASE %(s)s'
    WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = '%(s)s')
    """ % {'s': app.config['DBDB']}
    cur.execute(sql)
    cur.close()
    conn0.commit()

    app.logger.info('Database created!')
    tblSetup()

    time.sleep(randrange(5))

def tblSetup():
    sql = """
        CREATE TABLE IF NOT EXISTS tiny(
   id SERIAL PRIMARY KEY,
   url VARCHAR NOT NULL
);
    """
    app.logger.info(sql)
    conn = psycopg2.connect(host=host, port=port, database=database,
                                        user=user, password=password)
    cur = conn.cursor()

    cur.execute(sql)
    cur.close()

    conn.commit()

    app.logger.info('Database setup!')
    time.sleep(1)