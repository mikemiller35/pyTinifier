from app import app
import time
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn0 = psycopg2.connect(
    host=app.config['DBHOST'],
    port=app.config['DBPORT'],
    database='postgres',
    user=app.config['DBUSER'],
    password=app.config['DBPASS']
)


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

    time.sleep(5)

def tblSetup():
    sql = """
        CREATE TABLE IF NOT EXISTS tiny(
   id SERIAL PRIMARY KEY,
   url VARCHAR NOT NULL
);
    """
    app.logger.info(sql)
    conn = psycopg2.connect(host=app.config['DBHOST'],
                            port=app.config['DBPORT'],
                            database=app.config['DBDB'],
                            user=app.config['DBUSER'],
                            password=app.config['DBPASS'])
    cur = conn.cursor()

    cur.execute(sql)
    cur.close()

    conn.commit()

    app.logger.info('Database setup!')
    time.sleep(1)