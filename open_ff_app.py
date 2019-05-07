#! /usr/bin/python3
# -*-coding: utf-8-*-

from api.open_ff_api import Open_FF_Api
from db.mysql_db import Mysql_db
from views.user_displays import User_displays
import config.open_ff_settings as constants
import config.db_settings as db_constants
import config.queries_settings as db_data_constants
from db.db_requests import DB_requests


def main():

    db = Mysql_db()
    User_displays(db)
    api = Open_FF_Api()

    cat_choice = User_displays.category_choice_nenu()


    data = api.search_products(constants.categories[cat_choice-1])
    db.insert_data_to_database(data)

    prod_choice = User_displays.list_of_products_menu( constants.categories[cat_choice-1])

    substitute_choice = User_displays.show_alternatives(prod_choice)


if __name__ == "__main__":
    main()
