#! /usr/bin/python3
# -*-coding: utf-8-*-

from os import system
from requests.exceptions import ConnectionError
import time
from api.open_ff_api import Open_FF_Api
from db.mysql_db import Mysql_db
from views.user_displays import User_displays
import config.open_ff_settings as constants
import config.db_settings as db_constants
import config.queries_settings as db_data_constants
import config.display_settings as display_constants
from db.db_requests import DB_requests


def main():
    # Initialize loop variables
    main_loop = 1
    data = 0

    # Instance DB and OpenFoodFacts API
    db = Mysql_db()
    api = Open_FF_Api()
    # Create de data base and the tables
    db.create_database()
    db.create_tables()
    # Initialize the menus
    User_displays(db)

    while main_loop:
        main_choice = User_displays.main_choice_menu()
        if main_choice == "Q":
            db.close_connection()
            exit()

        elif main_choice == 1:
            # Try to connect to OpenFoodFacts, search products and insert them in local database.
            try:
                for category in constants.categories:
                    # Search data from OpenFoodFacts and insert them in local database
                    User_displays.system_info("Api_Search")
                    data = api.search_products(category)
                    User_displays.system_info("Table_update", category)
                    db.insert_data_to_database(data)
            except ConnectionError as error:
                #print(error)
                print("Connection à OpenFoodFacts non disponible !")
                time.sleep(2)
            User_displays.system_info("Update_completed")
            main_choice == 0

        elif main_choice == 2:
            cat_choice = 0
            prod_choice_id = 0
            substitute_choice_id = 0
                # Display category choice menu
            cat_choice = User_displays.category_choice_nenu()
            if cat_choice:
                # Display products choice menu
                prod_choice_id = User_displays.products_choice_menu( constants.categories[cat_choice-1])
            if prod_choice_id:
                # Display substitutes choice menu
                substitute_choice_id = User_displays.substitutes_choice_menu(prod_choice_id)
            if substitute_choice_id:
                # Display comparison and save menu
                User_displays.comparison_and_save_menu(substitute_choice_id)

        else:
            User_displays.favorites()

        main_choice = 0


if __name__ == "__main__":
    main()
