#! /usr/bin/python3
# -*-coding: utf-8-*-

import config.queries_settings as queries_constants


class DB_requests:
    """This class contains method to find the products and favorites in
    database, allow to flip through the result pages and save the substitutes  """
    def __init__(self, db_instance):
        self.db = db_instance

    def find_products(self, query, id, category=None):
        self.db.cursor.execute(query, {"id": id, "category": category})
        result = self.db.cursor.fetchall()
        return result

    def find_substitutes(self, query, id, category = None):
        startchar = 1
        endchar = 6
        while 1:
            self.db.cursor.execute(queries_constants.FIND_GENERIC_WORD,{"id": id, "startchar" : startchar ,"endchar" : endchar})
            word = self.db.cursor.fetchall()
            word1, = word[0]
            self.db.cursor.execute(query, {"id": id, "category": category, "word" : word1})
            result = self.db.cursor.fetchall()
            if len(result) >= 1 and len(result) <= 20 :
                break
            if endchar < 100:
                startchar = startchar + 5
                endchar = endchar + 5
            else:
                startchar = 0
                endchar = 0
        print("mot clé : " ,word1)
        return result

    def find_all_favorites(self):
        self.db.cursor.execute(queries_constants.FIND_FAVORITE_BY_ID)
        result = self.db.cursor.fetchall()
        favorites = []
        for prod_id, subst_id in result:
            #print(prod_id, subst_id)
            favorites.append([self.find_products(
                queries_constants.FIND_PRODUCTS_BY_ID, prod_id, None), self.find_products(
                    queries_constants.FIND_PRODUCTS_BY_ID, subst_id, None)])
        return favorites

    def save_substitute(self, product_id, substitute_id):
        self.db.cursor.execute(
            queries_constants.SAVE_SUBSTITUTE, {
                "id_prod": product_id, "id_subst": substitute_id})
        self.db.connect.commit()
