import psycopg2
from app import app


class MyDatabase:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(host=app.config['DBHOST'], port=app.config['DBPORT'],
                                         database=app.config['DBDB'],
                                         user=app.config['DBUSER'], password=app.config['DBPASS'])
        except (Exception, psycopg2.DatabaseError) as error:
            app.logger.warning("~ Can't connect to the DB! ~")
            app.logger.warning(error)

    def query(self, query):
        self.cur = self.conn.cursor()
        self.cur.execute(query)
        result = self.cur.fetchall()
        self.close()
        return result

    def modifyq(self, query):
        self.cur = self.conn.cursor()
        self.cur.execute(query)
        self.conn.commit()
        self.close()

    def close(self):
        self.cur.close()
        self.conn.close()
