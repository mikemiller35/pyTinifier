from app import app
import sqlite3


def dbCheck():
    create_table = """
        CREATE TABLE TINY(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        URL TEXT NOT NULL
        );
        """
    with sqlite3.connect(app.config['SQLITE']) as conn:
        cursor = conn.cursor()
        try:
            app.logger.info('Creating DB')
            cursor.execute(create_table)
        except Exception as e:
            app.logger.info("Exception in _query: %s" % e)
            pass
