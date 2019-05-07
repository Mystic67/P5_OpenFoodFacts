#! /usr/bin/python3
# -*-coding: utf-8-*-

#-------------------- TABLES DATA INSERT QUERIES---------------------------

INSERT_IN_PRODUCTS= """INSERT IGNORE INTO OpenFoodFacts.products (product_name, generic_name, brands, nutrition_grades, allergens, url) VALUES (%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE product_name = VALUES(product_name);"""


INSERT_IN_CATEGORIES= """INSERT IGNORE INTO OpenFoodFacts.categories (category) VALUES (%(cat)s) ON DUPLICATE KEY UPDATE category = VALUES(category);"""


INSERT_IN_PROD_CAT= """INSERT IGNORE INTO products_categories (product_id, category_id) VALUES ( %(id_prod)s, (SELECT categories.id FROM categories WHERE category = %(cat)s ));"""


INSERT_IN_STORES= """INSERT IGNORE INTO OpenFoodFacts.stores (store) VALUES (%(store)s) ON DUPLICATE KEY UPDATE store = VALUES(store);"""


INSERT_IN_PROD_STORE= """INSERT IGNORE INTO products_stores (product_id, store_id) values ( %(id_prod)s, ( SELECT stores.id FROM stores WHERE store = %(store)s ));"""

SAVE_ALTERNATIVE= """INSERT IGNORE INTO substitutes (product_id, alternative_id) values (%s, %s) ON DUPLICATE KEY UPDATE product_id = VALUES(product_id) and alternative_id = VALUES(alternative_id);"""


#--------------------SELECT QUERIES----------------------------------------

# Recherche toutes les catégories donc l'index de prodution est 1
SEARCH_CATEGORIES = """SELECT DISTINCT cat.category, prod.product_name FROM OpenFoodFacts.products as prod \
    INNER JOIN products_categories as prodcat \
    ON prodcat.product_id = prod.id \
    INNER JOIN categories as cat \
    ON prodcat.category_id = cat.id \
    WHERE  prod.id =1;"""

# Recherche toutes les catégories donc le nom de production commence par "J" avec les magazins ou le trouver
SEARCH_CATEGORIES_BY_PROD_NAME = """SELECT DISTINCT cat.category, prod.product_name, sto.store FROM \ OpenFoodFacts.products as prod \
    INNER JOIN products_categories as prodcat \
    ON prodcat.product_id = prod.id \
    INNER JOIN categories as cat \
    ON prodcat.category_id = cat.id \
    INNER JOIN products_stores as prodsto \
    ON prodsto.product_id = prod.id \
    INNER JOIN stores as sto \
    ON sto.id = prodsto.store_id \
    WHERE  prod.product_name like "j%"; """

FIND_ALL_PRODUCTS_BY_CATEGORIE = """SELECT DISTINCT prod.* FROM OpenFoodFacts.products as prod \
    INNER JOIN products_categories as prodcat \
    ON prodcat.product_id = prod.id \
    INNER JOIN categories as cat \
    ON prodcat.category_id = cat.id \
    WHERE cat.category like %s \
    ORDER BY prod.id \
    LIMIT %s \
    OFFSET %s;"""

FIND_PRODUCTS_BY_ID = """SELECT DISTINCT * FROM \
    OpenFoodFacts.products as prod \
    INNER JOIN products_categories as prodcat \
    ON prodcat.product_id = prod.id \
    INNER JOIN categories as cat \
    ON prodcat.category_id = cat.id \
    INNER JOIN products_stores as prodsto \
    ON prodsto.product_id = prod.id \
    INNER JOIN stores as sto \
    ON sto.id = prodsto.store_id \
    WHERE  prod.id = %s; """
