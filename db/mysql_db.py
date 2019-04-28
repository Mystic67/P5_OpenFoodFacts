#! /usr/bin/python3
# -*-coding: utf-8-*-

import mysql.connector
from mysql.connector import errorcode
import config.db_settings as db_constants

class Mysql_db:

    def __init__(self):
        self.connect = self.connection()
        self.cursor = self.connect.cursor()
        self.create_database()
        self.create_tables()

    def connection(self):
        try:
            cnx = mysql.connector.connect(**db_constants.SERVER_ACCES)
            return cnx
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Non d'utilisateur ou mot de passe d'accès à la DB erroné")
    
    def create_database(self):
        try: 
            self.cursor.execute("USE {}".format(db_constants.DB_NAME))
            print("Connecté à la base de données {}".format(db_constants.DB_NAME))
        except mysql.connector.Error as err:
            if err.errno == 1044:
                print("Vous n'avez pas les droits d'accès à la base de donnée. Vérifier vos droit.")

            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("La base de données {} n'existe pas.".format(db_constants.DB_NAME))
                print("Création de la base de données....")    
                self.cursor.execute(db_constants.CREATE_DB)
                print("Base de données crée")
                self.connect.database = db_constants.DB_NAME

    def create_tables(self):
        for table_query in db_constants.TABLES:
            self.cursor.execute( db_constants.TABLES[table_query] )

    def insert_data_in_table(self, table, collum_name, data_value):
        pass


    def close_connection(self):
        self.connect.close()