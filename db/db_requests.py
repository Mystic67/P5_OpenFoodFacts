#! /usr/bin/python3
# -*-coding: utf-8-*-

import config.queries_settings as queries_constants


class DB_requests:
    """This class contains methods to find the products and favorites and save the substitutes in database """

    def __init__(self, db_instance):
        self.db = db_instance

    def find_products(self, query, id, category=None):
        self.db.cursor.execute(query, {"id": id, "category": category})
        result = self.db.cursor.fetchall()
        return result

    def find_substitutes(self, query, id, category=None):
        key_words = self.get_key_words(id)
        while 1:
            for word in key_words:
                self.db.cursor.execute(
                    query, {"id": id, "category": category, "word": word})
                result = self.db.cursor.fetchall()
                if len(result) >= 1 and len(result) <= 20:
                    break
                # if last key_words tested and result < 1
                elif word == key_words[-1] and len(result) < 1:
                    word = " "
                    self.db.cursor.execute(
                        query, {"id": id, "category": category, "word": word})
                    result = self.db.cursor.fetchall()
            break
        return result

    def get_key_words(self, id):
        self.db.cursor.execute(
            queries_constants.FIND_GENERIC_NAME, {"id": id})
        [result] = self.db.cursor.fetchall()
        result = result[0].split()
        key_words = []
        for word in result:
            if len(word) > 3:
                key_words.append(word)
        return key_words

    def get_all_favorites(self):
        self.db.cursor.execute(queries_constants.FIND_FAVORITE_BY_ID)
        result = self.db.cursor.fetchall()
        favorites = []
        for prod_id, subst_id in result:
            favorites.append([self.find_products(
                queries_constants.FIND_PRODUCTS_BY_ID, prod_id, None), self.find_products(
                    queries_constants.FIND_PRODUCTS_BY_ID, subst_id, None)])
        return favorites

    def save_substitute(self, product_id, substitute_id):
        self.db.cursor.execute(
            queries_constants.SAVE_SUBSTITUTE, {
                "id_prod": product_id, "id_subst": substitute_id})
        self.db.connect.commit()
