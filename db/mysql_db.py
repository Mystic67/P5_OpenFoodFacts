#! /usr/bin/python3
# -*-coding: utf-8-*-

import mysql.connector
from mysql.connector import errorcode
import config.open_ff_settings as constants
import config.db_settings as db_constants
import config.queries_settings as db_data_constants
import config.display_settings as display_constants


class Mysql_db:
    '''This class connect user to database, create the database
    and the tables and put the OpenFoodFacts data into the tables'''

    def __init__(self):
        self.connect = self.connection()
        self.cursor = self.connect.cursor()

    def connection(self):
        try:
            cnx = mysql.connector.connect(**db_constants.SERVER_ACCES)
            return cnx
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Non d'utilisateur ou mot de passe d'accès \
                à la DB erroné")

    def create_database(self):
        try:
            self.cursor.execute("USE {}".format(db_constants.DB_NAME))
            print(
                display_constants.colours["black"],
                display_constants.colours["on_yellow"],
                display_constants.colours["blink"],
                "Création de la base de données {}. Veuillez patienter !".format(
                    db_constants.DB_NAME),
                display_constants.colours["default"],
            )
        except mysql.connector.Error as err:
            if err.errno == 1044:
                print(
                    "Vous n'avez pas les droits d'accès à la base de \
                    donnée. Vérifier vos droit.")

            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print(
                    "La base de données {} n'existe pas.".format(
                        db_constants.DB_NAME))
                print(
                    "Création de la base de données {}".format(
                        db_constants.DB_NAME))
                self.cursor.execute(db_constants.CREATE_DB)
                print("Base de données à été crée")
                self.connect.database = db_constants.DB_NAME

    def create_tables(self):
        for table_query in db_constants.TABLES:
            self.cursor.execute(db_constants.TABLES[table_query])

    def insert_data_to_database(self, api_data):
        for data in api_data:
            list_row_values = []
            for api_key in constants.fr_food_informations.values():
                if api_key in data.keys():
                    if api_key == "categories":
                        list_cat = [cat.strip().strip("fr:").capitalize() for cat in data[api_key].split(",")]
                    elif api_key == "stores":
                        list_stores = [store.strip().upper() for store in data[api_key].split(",")]
                    else:
                        if api_key == "nutrition_grades":
                            list_row_values.append(data[api_key].upper())
                        else:
                            list_row_values.append(data[api_key])
            self.insert_in_tables(list_row_values, list_cat, list_stores)

    def insert_in_tables(self, product, categories, stores):
        # Insert product in table
        self.cursor.execute(
            db_data_constants.INSERT_IN_PRODUCTS,
            product)
        last_product_row_id = self.cursor.lastrowid
        # Insert categories in table
        for category in categories:
            self.cursor.execute(
                db_data_constants. INSERT_IN_CATEGORIES, {
                    "cat": category})
            # Insert the id's in linking table
            self.cursor.execute(
                db_data_constants.INSERT_IN_PROD_CAT, {
                    "id_prod": last_product_row_id, "cat": category})
        # Insert stores in table
        for store in stores:
            self.cursor.execute(
                db_data_constants.INSERT_IN_STORES, {
                    "store": store})
            # Insert the id's in linking table
            self.cursor.execute(
                db_data_constants.INSERT_IN_PROD_STORE, {
                    "id_prod": last_product_row_id, "store": store})
        self.connect.commit()

    def close_connection(self):
        self.connect.close()
