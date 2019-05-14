#! /usr/bin/python3
# -*-coding: utf-8-*-
import mysql.connector
from mysql.connector import errorcode
import config.queries_settings as queries_constants


class DB_requests:
    def __init__(self, db_instance):
        self.db = db_instance
        self.offset = 0

    def find_products(self, query, id , category = None, limit = 8):
        self.db.cursor.execute(query, { "id" : id, "category" : category, "limit" : limit, "offset" : self.offset })
        result = self.db.cursor.fetchall()
        self.db.cursor.execute(query, { "id" : id, "category" : category, "limit" : 1000, "offset" : 0 })
        max_counter = len(self.db.cursor.fetchall())
        self.nb_of_results = len(result)
        self.limit = limit
        return (result, max_counter)

    def get_max_counter_request(self):
        return self.max_counter

    def increment_page(self):
        if self.nb_of_results == 0:
            self.offset = self.offset
        else:
            self.offset = self.offset + self.limit
        return self.offset

    def decrement_page(self):
        if self.offset <= 0:
            self.offset = 0
        else:
            self.offset = self.offset - self.limit

    def reset_offset(self):
        self.offset = 0

    def save_substitute(self, query, product_id, substitute_id):
        self.db.cursor.execute(query,{"id_prod" : product_id, "id_subst" : substitute_id })
        self.db.connect.commit()

    def find_favorite(self, query, limit = 1):
        self.db.cursor.execute(query, { "limit" : limit, "offset" : self.offset })
        mem_offset = self.offset
        result = self.db.cursor.fetchall()
        [(prod_id, subst_id)] = result
        self.nb_of_results = len(result)
        self.db.cursor.execute(query, { "limit" : 1000, "offset" : 0 })
        max_counter = len(self.db.cursor.fetchall())
        self.reset_offset()
        product, counter1 = self.find_products(queries_constants.FIND_PRODUCTS_BY_ID, prod_id, None, 1)
        substitute, counter2 = self.find_products(queries_constants.FIND_PRODUCTS_BY_ID, subst_id, None, 1)
        self.offset = mem_offset
        return (product, substitute, max_counter)
