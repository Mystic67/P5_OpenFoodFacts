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
        startchar = 1
        lenstring = 6
        first_loop = 0
        while True:
            self.db.cursor.execute(
                queries_constants.FIND_GENERIC_WORD, {
                    "id": id, "startchar": startchar, "lenstring": lenstring})
            word = self.db.cursor.fetchall()
            word1, = word[0]
            self.db.cursor.execute(
                query, {"id": id, "category": category, "word": word1})
            result = self.db.cursor.fetchall()
            print("NB résultat = ", len(result))
            if len(result) >= 1 and len(result) <= 20:
                break
            # If all words texted and result = 0 or > 20
            elif first_loop and len(result) >= 0:
                break
            elif startchar < 290:
                startchar = startchar + 6
            elif startchar > 290:
                first_loop = first_loop + 1
                startchar = 1

        return result

    def find_all_favorites(self):
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
