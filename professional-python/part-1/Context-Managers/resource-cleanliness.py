"""
It is often important that the handle in question is closed properly, to avoid ending up
with a situation where many zombie problems can araise
Example: Closing a database connection which was opened
"""

import psycopg2

class PostgreSQLDBConnection(object):

    def __init__(self, dbname = None, user = None, password = None, host = 'localhost'):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password

    def __enter__(self):
        self.connection = psycopg2.connect(dbname = self.dbname,
                                            host = self.host,
                                            user = self.user,
                                           password = self.password)
        return self.connection.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

with PostgreSQLDBConnection(user='mj', dbname = 'foo') as db:
    db.execute('SELECT 1 + 1')
    db.fetchall()

# below command will raise an Interface error because the connection ended after the context manager
db.execute('SELECT 1 + 1')