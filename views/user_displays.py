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
    '''This class display the selection menus of choice, \
    find chosen data in database and display them'''

    @classmethod
    def __init__(cls, database):
        cls.database = database
        cls.db_request = DB_requests(cls.database)

    @classmethod
    def main_choice_menu(cls):
        system('cls||clear')
        cls.message("Welcome")
        cls.text_menu("Main_menu")
        cls.separate_text("Main_question")
        list_headers = ["       Choix N°     ", "     Faites votre choix     "]
        rows = []
        for index, choice in enumerate(display_constants.main_choice_text):
            rows.append([index + 1, choice])
        cls.display_products(rows, list_headers)
        while 1:
            try:
                choice = input(display_constants.messages['Main_choice'])
                if str(choice.upper()) == "Q":
                    return choice.upper()
                    break
                else:
                    choice = int(choice)
                if choice in range(
                    1, len(
                        display_constants.main_choice_text) + 1):
                    print("Vous avez choisi '{}': ".format(
                        display_constants.main_choice_text[choice - 1].strip("\t")))
                    time.sleep(1)
                    return choice
                    break
                else:
                    cls.message_error("ValueError")
            except ValueError:
                cls.message_error("ValueError")
            time.sleep(2)

    @classmethod
    def category_choice_nenu(cls):
        system('cls||clear')
        cls.message("Welcome")
        cls.text_menu("Category_choice")
        list_headers = ["     Choix N°     ", "     Catégories     "]
        rows = []
        for index, categorie in enumerate(constants.categories):
            rows.append([index + 1, categorie])
        cls.display_products(rows, list_headers, 'c')
        while 1:
            try:
                choice = input(display_constants.messages['Category_choice'])
                if str(choice.upper()) == "Q":
                    choice = 0
                    return choice
                    break
                else:
                    choice = int(choice)
                if choice in range(1, len(constants.categories) + 1):
                    print("Vous avez choisi '{}': ".format(
                        constants.categories[choice - 1]))
                    time.sleep(1)
                    return choice
                    break
                else:
                    cls.message_error("ValueError")
            except ValueError:
                cls.message_error("ValueError")
            time.sleep(2)

    @classmethod
    def products_choice_menu(cls, category):
        cls.category = category
        cls.db_request.reset_offset()
        products, counter = cls.db_request.find_products(
            queries_constants.FIND_ALL_PRODUCTS_BY_CATEGORIE, None, category)
        list_rows = ['Index'] + \
            [row for row in constants.fr_food_informations.keys()]
        while 1:
            list_ids = []
            [list_ids.append(prods[0]) for prods in products]
            system('cls||clear')
            cls.message("Welcome")
            cls.counter(counter)
            cls.text_menu("Food_choice")
            cls.display_products(products, (list_rows[:6] + list_rows[9:]))
            try:
                choice = input(
                    display_constants.colours["black"] +
                    display_constants.colours["on_cyan"] +
                    display_constants.messages["Pagination_info"] +
                    "\n" +
                    display_constants.colours["default"] +
                    display_constants.messages['Product_choice'])
                if str(choice.upper()) == "Q":
                    choice = 0
                    return choice
                    break
                elif choice == "+":
                    cls.db_request.increment_page()
                    products, counter = cls.db_request.find_products(
                        queries_constants.FIND_ALL_PRODUCTS_BY_CATEGORIE, None, category)
                elif choice == "-":
                    cls.db_request.decrement_page()
                    products, counter = cls.db_request.find_products(
                        queries_constants.FIND_ALL_PRODUCTS_BY_CATEGORIE, None, category)
                else:
                    choice = int(choice)
                    if choice in list_ids:
                        print("Vous avez choisi '{}': ".format(choice))
                        cls.db_request.reset_offset()
                        time.sleep(1)
                        return choice
                        break
                    else:
                        cls.message_error("ValueError")
            except ValueError:
                cls.message_error("ValueError")
            time.sleep(1)

    @classmethod
    def substitutes_choice_menu(cls, prod_choice_id):
        cls.prod_choice_id = prod_choice_id
        product, counter = cls.db_request.find_products(
            queries_constants.FIND_PRODUCTS_BY_ID, prod_choice_id, cls.category)
        cls.db_request.reset_offset()
        substitutes, counter = cls.db_request.find_products(
            queries_constants.FIND_SUBSTITUTES_BY_ID, prod_choice_id, cls.category)
        list_rows = ['Index'] + \
            [row for row in constants.fr_food_informations.keys()]
        while 1:
            list_ids = []
            [list_ids.append(prods[0]) for prods in substitutes]
            system('cls||clear')
            cls.message("Welcome")
            cls.counter(counter)
            cls.text_menu("Substitute_choice")
            cls.separate_text("Product")
            cls.display_products(
                [product[0][:6] + product[0][9:]], (list_rows[:6] + list_rows[9:]))
            cls.separate_text("Substitute")
            cls.display_products(substitutes, (list_rows[:6] + list_rows[9:]))
            try:
                choice = input(
                    display_constants.colours["black"] +
                    display_constants.colours["on_cyan"] +
                    display_constants.messages["Pagination_info"] +
                    "\n" +
                    display_constants.colours["default"] +
                    display_constants.messages['Substitute_choice'])
                if str(choice.upper()) == "Q":
                    choice = 0
                    return choice
                    break
                elif choice == "+":
                    cls.db_request.increment_page()
                    substitutes, counter = cls.db_request.find_products(
                        queries_constants.FIND_SUBSTITUTES_BY_ID, prod_choice_id, cls.category)
                elif choice == "-":
                    cls.db_request.decrement_page()
                    substitutes, counter = cls.db_request.find_products(
                        queries_constants.FIND_SUBSTITUTES_BY_ID, prod_choice_id, cls.category)
                elif int(choice) in list_ids:
                    choice = int(choice)
                    print("Vous avez choisi '{}': ".format(choice))
                    cls.db_request.reset_offset()
                    time.sleep(1)
                    return choice
                    break
                else:
                    cls.message_error("ValueError")
            except ValueError:
                cls.message_error("ValueError")
            time.sleep(1)

    @classmethod
    def comparison_and_save_menu(cls, substitute_id):
        cls.substitute_id = substitute_id
        cls.db_request.reset_offset()
        product_details, counter = cls.db_request.find_products(
            queries_constants.FIND_PRODUCTS_BY_ID, cls.prod_choice_id, cls.category)
        substitute_details, counter = cls.db_request.find_products(
            queries_constants.FIND_PRODUCTS_BY_ID, substitute_id, cls.category)

        list_rows_names = ['Index'] + \
            [row for row in constants.fr_food_informations.keys()]
        columns_name = [
            "  ",
            "Aliment à substituer",
            "Aliment de substitution"]
        while 1:
            system('cls||clear')
            cls.message("Welcome")
            cls.text_menu("product_comparison")
            # Create rows
            list_rows = []
            i = 0
            while i < len(substitute_details[0]):
                list_rows.append([list_rows_names[i], product_details[0]
                                  [i], substitute_details[0][i]])
                i = i + 1
            cls.display_products(list_rows, columns_name)
            try:
                choice = input(
                    display_constants.colours["black"] +
                    display_constants.colours["on_cyan"] +
                    display_constants.messages["Pagination_info"] +
                    "\n" +
                    display_constants.colours["default"] +
                    display_constants.messages['Save_substitute'])
                if str(choice.upper()) == "Q":
                    choice = 0
                    return choice
                    break
                else:
                    choice = str(choice)
                    if choice.upper() == "OUI":
                        try:
                            cls.db_request.save_substitute(
                                queries_constants.SAVE_SUBSTITUTE, cls.prod_choice_id, substitute_id)
                            cls.message("Confim_saved", "black", "on_yellow",
                                        cls.prod_choice_id, substitute_id)
                        except BaseException:
                            cls.message_error("Save_error")
                        time.sleep(3)
                        break
                    else:
                        cls.message_error("ValueError")
            except ValueError:
                cls.message_error("ValueError")
            time.sleep(1)

    @classmethod
    def favorites(cls):
        cls.db_request.reset_offset()
        product, substitute, counter = cls.db_request.find_favorite(
            queries_constants.FIND_FAVORITE_BY_ID, 1)
        list_rows_names = ['Index'] + \
            [row for row in constants.fr_food_informations.keys()]
        columns_name = ["  ", "Aliment substitué", "Aliment de substitution"]
        while 1:
            system('cls||clear')
            cls.message("Welcome")
            cls.text_menu("products_saved")
            list_rows = []
            i = 0
            while i < len(list_rows_names):
                list_rows.append(
                    [list_rows_names[i], product[0][i], substitute[0][i]])
                i = i + 1
            cls.display_products(list_rows, columns_name)
            try:
                choice = input(
                    display_constants.colours["black"] +
                    display_constants.colours["on_cyan"] +
                    display_constants.messages["Pagination_info"] +
                    "\n" +
                    display_constants.colours["default"] +
                    display_constants.messages['Favorites'])
                choice = str(choice)
                if choice.upper() == "Q":
                    return choice
                    break
                elif choice == "+":
                    cls.db_request.increment_page()
                    product, substitute, counter = cls.db_request.find_favorite(
                        queries_constants.FIND_FAVORITE_BY_ID, 1)
                    print(counter)
                elif choice == '-':
                    cls.db_request.decrement_page()
                    product, substitute, counter = cls.db_request.find_favorite(
                        queries_constants.FIND_FAVORITE_BY_ID, 1)
                else:
                    cls.message_error("ValueError")
            except ValueError:
                cls.message_error("ValueError")
            time.sleep(1)

    @classmethod
    def display_products(cls, list_rows, list_headers, justify='c'):
        table = columnar(list_rows, headers=list_headers, justify=justify)
        print(table)

    @classmethod
    def text_menu(cls, text_menus):
        text_message = print("\t\t\t\t\t\t\t\t\t" +
                             # display_constants.colours["bold"]+
                             display_constants.colours["white"] +
                             display_constants.colours["on_magenta"] +
                             display_constants.text_menus[text_menus] +
                             display_constants.colours["default"] +
                             "\n")
        return text_message

    @classmethod
    def message(
            cls,
            message,
            color="black",
            background_color="on_cyan",
            *params):
        text_message = print(
            "\n" +
            display_constants.colours["bold"] +
            display_constants.colours[color] +
            display_constants.colours[background_color] +
            display_constants.messages[message].format(
                *
                params) +
            display_constants.colours["default"] +
            "\n")
        return text_message

    @classmethod
    def message_error(cls, error_message):
        text_message_error = print(
            display_constants.return_to_preview_line +
            display_constants.del_line +
            display_constants.colours["bold"] +
            display_constants.colours["white"] +
            display_constants.colours["on_red"] +
            display_constants.colours["blink"] +
            display_constants.errors[error_message] +
            display_constants.colours["default"] +
            display_constants.return_to_preview_line)
        return text_message_error

    @classmethod
    def counter(cls, counter):
        text_message = print(display_constants.colours["bold"] +
                             display_constants.colours["black"] +
                             display_constants.colours["on_yellow"] +
                             display_constants.counter.format(counter) +
                             display_constants.colours["default"])
        return text_message

    @classmethod
    def separate_text(cls, message):
        text_message = print("\t\t\t\t\t\t" +
                             display_constants.colours["white"] +
                             display_constants.colours["on_blue"] +
                             "\t\t\t" +
                             display_constants.separate_text[message] +
                             "\t\t\t" +
                             display_constants.colours["default"] +
                             "\t\t\t\t\t\t")
        return text_message

    @classmethod
    def system_info(cls, message, *param):
        text_message = print(
            display_constants.del_line +
            display_constants.colours["black"] +
            display_constants.colours["on_yellow"] +
            display_constants.colours["blink"] +
            display_constants.system_info[message].format(
                *
                param) +
            display_constants.return_to_preview_line +
            display_constants.colours["default"])
        return text_message
