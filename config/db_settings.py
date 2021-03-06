#! /usr/bin/python3
# -*-coding: utf-8-*-


SERVER_ACCES = {
  'host': '127.0.0.1',
  'user': 'Pure_beurre',
  'password': 'Projet_5-OC'
}

DB_NAME = 'OpenFoodFacts'

# Create DATABASE if not exists
CREATE_DB = "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8mb4' \
                    COLLATE 'utf8mb4_unicode_ci'".format(DB_NAME)


# Store table creation queries in dictionnary
TABLES = {}
TABLES['store'] = (
    "CREATE TABLE IF NOT EXISTS stores ( \
        id INT UNSIGNED AUTO_INCREMENT, \
        store VARCHAR(50) UNIQUE NOT NULL, \
        PRIMARY KEY (id) ) \
    ENGINE=InnoDB;"
    )

TABLES['categories'] = (
    "CREATE TABLE IF NOT EXISTS categories ( \
        id INT UNSIGNED AUTO_INCREMENT, \
        category VARCHAR(50) UNIQUE NOT NULL, \
        PRIMARY KEY (id) \
        ) \
    ENGINE=InnoDB;"
    )

TABLES['products'] = (
    "CREATE TABLE IF NOT EXISTS products ( \
        id INT UNSIGNED AUTO_INCREMENT, \
        product_name VARCHAR(150) UNIQUE NOT NULL, \
        generic_name VARCHAR(300) NOT NULL, \
        brands VARCHAR(50) NOT NULL, \
        nutrition_grades CHAR(1) NOT NULL, \
        allergens VARCHAR(255) NULL, \
        ingredients_text_fr VARCHAR(500) NOT NULL, \
        url VARCHAR(255) NOT NULL, \
        PRIMARY KEY (id) \
        ) \
    ENGINE=InnoDB;"
    )

TABLES['substitutes'] = (
    "CREATE TABLE IF NOT EXISTS substitutes ( \
        id INT UNSIGNED AUTO_INCREMENT, \
        product_id INT UNSIGNED NOT NULL, \
        substitute_id INT UNSIGNED NOT NULL, \
        PRIMARY KEY (id), \
        UNIQUE KEY (product_id, substitute_id), \
        CONSTRAINT product_products_id_fk \
        FOREIGN KEY (product_id) \
        REFERENCES products (id), \
        CONSTRAINT substitute_products_id_fk \
        FOREIGN KEY (substitute_id) \
        REFERENCES products (id) \
        ) \
    ENGINE=InnoDB;"
    )

TABLES['products_categories'] = (
    "CREATE TABLE IF NOT EXISTS products_categories ( \
        id INT UNSIGNED AUTO_INCREMENT, \
        product_id INT UNSIGNED NOT NULL, \
        category_id INT UNSIGNED NOT NULL, \
        PRIMARY KEY (id), \
        UNIQUE KEY (product_id, category_id), \
        CONSTRAINT categories_products_categories_fk \
        FOREIGN KEY (category_id) \
        REFERENCES categories (id), \
        CONSTRAINT products_products_categories_fk \
        FOREIGN KEY (product_id) \
        REFERENCES products (id) \
        ) \
    ENGINE=InnoDB;"
    )

TABLES['products_stores'] = (
    "CREATE TABLE IF NOT EXISTS products_stores ( \
        id INT UNSIGNED AUTO_INCREMENT, \
        product_id INT UNSIGNED NOT NULL, \
        store_id INT UNSIGNED NOT NULL, \
        PRIMARY KEY (id), \
        UNIQUE KEY (product_id, store_id), \
        CONSTRAINT stores_products_stores_fk \
        FOREIGN KEY (store_id) \
        REFERENCES stores (id), \
        CONSTRAINT products_products_stores_fk \
        FOREIGN KEY (product_id) \
        REFERENCES products (id) \
        ) \
    ENGINE=InnoDB;"
    )
