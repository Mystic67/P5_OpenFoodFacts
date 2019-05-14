#! /usr/bin/python3
# -*-coding: utf-8-*-

#Open Food Facts settings:
url= "https://fr.openfoodfacts.org/cgi/search.pl?"

default_search_params= {
"tagtype_0" : "categories",
"countries" : "France",
"tag_contains_0" : "contains",
"search_simple" : "1",
"action" : "process",
"page_size" : "1000",
"page" : "1",
"json" : "1"
}

#User choise
categories=["Viandes","Plats préparés","Petit-déjeuners","Desserts","Fromages"]

# Desired food information:
fr_food_informations = { "Non du produit" : "product_name",
                        "Nom générique" : "generic_name",
                        "Marques" : "brands",
                        "Note\n(A à E)" : "nutrition_grades",
                        "Allergènes" : "allergens",
                        "Ingredients" : "ingredients_text_fr",
                        "URL Open Food Facts" : "url",
                        "Magasin" : "stores",
                        "Catégories" : "categories"
                         }
