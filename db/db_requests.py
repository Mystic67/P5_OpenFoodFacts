#! /usr/bin/python3
# -*-coding: utf-8-*-
import mysql.connector
from mysql.connector import errorcode
import config.queries_settings as queries_constants

class DB_requests:
    def __init__(self, db_instance):
        self.db = db_instance
        self.offset =0

    def find_products(self, query, category, limit = 9):
        self.db.cursor.execute(query,(category, limit, self.offset ))
        result = self.db.cursor.fetchall()
        self.db.cursor.execute(query,(category, 1000, 0 ))
        max_counter = len(self.db.cursor.fetchall())
        self.nb_of_results = len(result)
        print("Nombre de résultat : {} max: {}".format(self.nb_of_results, max_counter))
        return (result, max_counter)

    def get_max_counter_request(self):
        print(self.max_counter)
        return self.max_counter

    def increment_page(self):
        if self.nb_of_results <= 0:
            self.offset = self.offset
        else:
            self.offset = self.offset + 10
        return self.offset

    def decrement_page(self):
        if self.offset <= 0:
            self.offset = 0
        else:
            self.offset = self.offset - 10

    def find_product_by_id(self, query, colums, product_id):
        self.db.cursor.excute(query, colums, product_id)

    def find_substitutes(self, query, product_id):
        pass
