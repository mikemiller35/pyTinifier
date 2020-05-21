import psycopg2
from app import app
from urllib.parse import urlparse


class MyDatabase:
    def __init__(self):
        if app.config['DBHOST'] is None or app.config['DBHOST'] == '':
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
        try:
            self.conn = psycopg2.connect(host, port, database, user, password)
            cur = self.conn.cursor()
        except (Exception, psycopg2.DatabaseError) as error:
            app.logger.warning("~ Can't connect to the DB! ~")
            app.logger.warning(error)
