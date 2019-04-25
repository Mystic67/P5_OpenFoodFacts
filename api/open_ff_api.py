#! /usr/bin/python3
# -*-coding: utf-8-*-
import requests
from columnar import columnar
import config.open_ff_settings as constants

class Open_FF_Api:
    def __init__(self):
        self.categorie = constants.categories

    def search_products(self, category="Viandes"):
        constants.default_search_params["tag_0"]= category
        req = requests.get(constants.url, constants.default_search_params)
        data_json = req.json()
        self.products_data = data_json['products']

        fistLoop = True
        data_table =[]
        for data in self.products_data:
            list_fields_name = []
            list_row =[]
            for key, value in constants.fr_food_informations.items():
                if value in data:
                    if fistLoop:
                        list_fields_name.append(key)
                    list_row.append(data[value])

            data_table.append(list_row)
        fistLoop = False 
        self.display_products(data_table, list_fields_name)


    def display_products(self, table_rows, list_headers):
        table = columnar( table_rows, headers = list_headers, justify ='c' )
        print(table)
