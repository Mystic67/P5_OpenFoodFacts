#! /usr/bin/python3
# -*-coding: utf-8-*-

import requests
import config.open_ff_settings as constants


class Open_FF_Api:
    '''This class connect to OpenfoodFacts API, recover the data from
    database and filter the data'''

    def __init__(self):
        self.categorie = constants.categories

    def search_products(self, category=""):
        '''Search the data from OpenFoodFacts database and return the
        data in json format '''
        constants.default_search_params["tag_0"] = category
        req = requests.get(constants.url, constants.default_search_params)
        data_json = req.json()
        products_data = data_json['products']
        filtered_data = self.filter_api_data(products_data)
        return filtered_data

    def filter_api_data(self, api_data):
        filtered_api_data = []
        for data in api_data:
            if all(key in data for key in constants.fr_food_informations.values()):
                if data['product_name'] and data['generic_name'] and data['brands'] and data[
                        'nutrition_grades'] and data['ingredients_text_fr'] and data['url'] and data['stores'] and data['categories']:
                    filtered_api_data.append(data)
        return filtered_api_data
