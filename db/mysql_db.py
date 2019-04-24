import mysql.connector
from mysql.connector import errorcode
import config.db_settings as db_constants

class Mysql_db:

    def __init__(self):
        self.db_connect = self.db_connection()
        self.db_cursor = self.db_connect.cursor()

    def db_connection(self):
        try:
            cnx = mysql.connector.connect(**db_constants.db_config)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            else:
                cnx.close()
        return cnx

    def close_db_connection(self):
        self.db_connect.close()

    def create_tables(self):
        pass
