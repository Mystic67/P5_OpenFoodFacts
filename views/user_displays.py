#! /usr/bin/python3
# -*-coding: utf-8-*-

from os import system
import time
from columnar import columnar
import config.display_settings as display_constants
import config.open_ff_settings as constants
import config.queries_settings as queries_constants
from db.db_requests import DB_requests


class User_displays:

    @classmethod
    def __init__(cls, database):
        cls.database = database
        cls.db_request = DB_requests(cls.database)
        cls.product_req = queries_constants.FIND_ALL_PRODUCTS_BY_CATEGORIE


    @classmethod
    def display_products(cls, list_rows, list_headers, justify = 'c'):
        table = columnar( list_rows, headers = list_headers, justify = justify )
        print(table)

    @classmethod
    def category_choice_nenu(cls):
        system('cls||clear')
        cls.message("Welcome")
        list_headers = ["    Choix N°   ","    Catégories    "]
        rows = []
        for index, categorie in enumerate(constants.categories):
            rows.append([index+1,categorie])
        cls.display_products(rows, list_headers,'c')

        while 1:
            try:
                choice = input(display_constants.messages['Category_choice'])
                if str(choice.upper()) == "Q":
                    break
                else:
                    choice = int(choice)
                if choice in range(1,len(constants.categories)+1):
                    print("Vous avez choisi '{}': ".format(constants.categories[choice-1]))
                    return choice
                    break
                else:
                    cls.message_error("ValueError")
            except ValueError:
                cls.message_error("ValueError")
            time.sleep(2)

    @classmethod
    def list_of_products_menu(cls, category):
        sql_result, counter = cls.db_request.find_products(cls.product_req, category)
        print(counter)
        list_rows = ['Index']+[row for row in constants.fr_food_informations.keys()]
        while 1:
            system('cls||clear')
            cls.message("Welcome")
            cls.counter(counter)
            cls.display_products(sql_result, list_rows)

            try:
                choice = input(display_constants.colours["black"] + display_constants.colours["on_cyan"] + display_constants.messages["Pagination_info"]+"\n"+ display_constants.colours["default"] + display_constants.messages['Product_choice'])
                if str(choice.upper()) == "Q":
                    break
                elif choice == "+":
                    offset = cls.db_request.increment_page()
                    sql_result, counter = cls.db_request.find_products(cls.product_req, category)
                elif choice == "-":
                    cls.db_request.decrement_page()
                    sql_result, counter = cls.db_request.find_products(cls.product_req, category)
                else:
                    choice = int(choice)
                if choice in range(len(constants.categories)+1):
                    if choice ==0:
                        break
                    else:
                        return choice
                        break
                else:
                    continue
            except ValueError:
                cls.message_error("ValueError")
            time.sleep(2)

    @classmethod
    def show_alternatives(cls, prod_choice):
         pass



    @classmethod
    def message(cls, message):
        message = print("\n"+display_constants.colours["bold"]+
        display_constants.colours["black"]+
        display_constants.colours["on_cyan"]+
        #display_constants.colours["blink"]+
        display_constants.messages[message]+
        display_constants.colours["default"]+
        "\n")
        return message

    @classmethod
    def message_error(cls, error_message):
        message_error = print(display_constants.colours["bold"]+
        display_constants.colours["white"]+
        display_constants.colours["on_red"]+
        display_constants.colours["blink"]+
        display_constants.errors[error_message]+
        display_constants.colours["default"]+
        display_constants.del_preview_line)
        return message_error

    @classmethod
    def counter(cls, counter):
        message = print(display_constants.colours["bold"]+
        display_constants.colours["black"]+
        display_constants.colours["on_yellow"]+
        #display_constants.colours["blink"]+
        display_constants.counter.format(counter)+
        display_constants.colours["default"])
        return message
