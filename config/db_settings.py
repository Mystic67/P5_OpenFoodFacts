#! /usr/bin/python3
# -*-coding: utf-8-*-


SERVER_ACCES = {
  'host': '127.0.0.1',
  'user': 'Pure_beurre',
  'password': 'Projet_5-OC'
}

DB_NAME = 'OpenFoodFacts'
CREATE_DB = "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8mb4' \
                    COLLATE 'utf8mb4_unicode_ci'".format(DB_NAME)

# Store table creation queries in dictionnary
TABLES = {}
TABLES['store'] = (
    "CREATE TABLE IF NOT EXISTS stores ( \
        id INT AUTO_INCREMENT NOT NULL, \
        store VARCHAR(50) UNIQUE NOT NULL, \
        PRIMARY KEY (id) ) \
    ENGINE=InnoDB;"
    )

TABLES['categories'] = (
    "CREATE TABLE IF NOT EXISTS categories ( \
        id INT AUTO_INCREMENT NOT NULL, \
        category VARCHAR(50) UNIQUE NOT NULL, \
        PRIMARY KEY (id) \
        ) \
    ENGINE=InnoDB;"
    )

TABLES['products'] = (
    "CREATE TABLE IF NOT EXISTS products ( \
        id BIGINT AUTO_INCREMENT NOT NULL, \
        product_name VARCHAR(200) UNIQUE NOT NULL, \
        generic_name VARCHAR(300) NOT NULL, \
        brands VARCHAR(50) NOT NULL, \
        nutrition_grades CHAR(1) NOT NULL, \
        allergens VARCHAR(255) NULL, \
        url VARCHAR(255) NOT NULL, \
        PRIMARY KEY (id) \
        ) \
    ENGINE=InnoDB;"
    )

TABLES['substitutes'] = (
    "CREATE TABLE IF NOT EXISTS substitutes ( \
        id BIGINT AUTO_INCREMENT NOT NULL, \
        products_id BIGINT NOT NULL, \
        alternative_id BIGINT NOT NULL, \
        PRIMARY KEY (id), \
        UNIQUE KEY products_id (products_id), \
        UNIQUE KEY alternative_id (alternative_id), \
        CONSTRAINT products_substitutes_fk \
        FOREIGN KEY (Products_id) \
        REFERENCES products (id) \
        ) \
    ENGINE=InnoDB;"
    )


TABLES['products_categories'] = (
    "CREATE TABLE IF NOT EXISTS products_categories ( \
        id BIGINT AUTO_INCREMENT NOT NULL, \
        product_id BIGINT NOT NULL, \
        category_id INT NOT NULL, \
        PRIMARY KEY (id), \
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
        id BIGINT AUTO_INCREMENT NOT NULL, \
        product_id BIGINT NOT NULL, \
        store_id INT NOT NULL, \
        PRIMARY KEY (id), \
        CONSTRAINT stores_products_stores_fk \
        FOREIGN KEY (store_id) \
        REFERENCES stores (id), \
        CONSTRAINT products_products_stores_fk \
        FOREIGN KEY (product_id) \
        REFERENCES products (id) \
        ) \
    ENGINE=InnoDB;"
    )
