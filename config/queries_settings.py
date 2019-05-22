#! /usr/bin/python3
# -*-coding: utf-8-*-


# -------------------- TABLES DATA INSERT QUERIES---------------------------

INSERT_IN_PRODUCTS = """INSERT IGNORE INTO OpenFoodFacts.products (product_name, generic_name, brands, nutrition_grades, allergens, ingredients_text_fr, url ) VALUES (%s,%s,%s,%s,%s,%s,%s) ;"""

INSERT_IN_CATEGORIES = """INSERT IGNORE INTO OpenFoodFacts.categories (category) VALUES (%(cat)s) ;"""

INSERT_IN_PROD_CAT = """INSERT IGNORE INTO products_categories (product_id, category_id) VALUES ( %(id_prod)s, (SELECT categories.id FROM categories WHERE category = %(cat)s ));"""

INSERT_IN_STORES = """INSERT IGNORE INTO OpenFoodFacts.stores (store) VALUES (%(store)s) ;"""

INSERT_IN_PROD_STORE = """INSERT IGNORE INTO products_stores (product_id, store_id) values ( %(id_prod)s, ( SELECT stores.id FROM stores WHERE store = %(store)s ));"""

SAVE_SUBSTITUTE = """INSERT IGNORE INTO substitutes (product_id, substitute_id) values (%(id_prod)s, %(id_subst)s) ;"""


# --------------------SELECT QUERIES----------------------------------------

FIND_ALL_PRODUCTS_BY_CATEGORIE = """SELECT DISTINCT prod.id, product_name, generic_name, brands, nutrition_grades, allergens, category FROM OpenFoodFacts.products as prod
    INNER JOIN products_categories as prodcat
    ON prodcat.product_id = prod.id
    INNER JOIN categories as cat
    ON prodcat.category_id = cat.id
    WHERE cat.category like %(category)s
    AND prod.nutrition_grades > 'B'
    ORDER BY prod.id ;"""

FIND_SUBSTITUTES_FOR_ID = """SELECT DISTINCT prod.id, product_name, generic_name, brands, nutrition_grades, allergens, category FROM
    OpenFoodFacts.products as prod
    INNER JOIN products_categories as prodcat
    ON prodcat.product_id = prod.id
    INNER JOIN categories as cat
    ON prodcat.category_id = cat.id
    INNER JOIN products_stores as prodsto
    ON prodsto.product_id = prod.id
    INNER JOIN stores as sto
    ON sto.id = prodsto.store_id
    WHERE category = %(category)s
    AND prod.nutrition_grades < (
    SELECT nutrition_grades FROM products as prod
    WHERE prod.id = %(id)s)
    AND generic_name like CONCAT('%',%(word)s,'%') ; """

FIND_PRODUCTS_BY_ID = """SELECT DISTINCT prod.id, product_name, generic_name, brands, nutrition_grades, allergens, ingredients_text_fr, url, GROUP_CONCAT(DISTINCT(store) SEPARATOR ', ') as store, GROUP_CONCAT(DISTINCT(category) SEPARATOR ', ') as category
    FROM OpenFoodFacts.products as prod
    INNER JOIN products_categories as prodcat
    ON prodcat.product_id = prod.id
    INNER JOIN categories as cat
    ON prodcat.category_id = cat.id
    INNER JOIN products_stores as prodsto
    ON prodsto.product_id = prod.id
    INNER JOIN stores as sto
    ON sto.id = prodsto.store_id
    WHERE  prod.id = %(id)s
    AND category = COALESCE(%(category)s, category)
    ORDER BY prod.id ; """

FIND_FAVORITE_BY_ID = """SELECT DISTINCT product_id, substitute_id FROM \
    OpenFoodFacts.substitutes
    ORDER BY substitute_id; """

FIND_GENERIC_NAME = """SELECT generic_name FROM products as prod
    WHERE prod.id = %(id)s; """
