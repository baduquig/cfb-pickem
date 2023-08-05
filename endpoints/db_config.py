import mysql.connector

class DBConfig():
    db_config = {
        'user': 'sql9634488',
        'password': '2usSRQH2hu',
        'host': 'sql9.freemysqlhosting.net',
        'database': 'sql9634488',
        'raise_on_warnings': True
    }

    def db_connect(self):
        conn = mysql.connector.connect(**self.db_config)
        return conn