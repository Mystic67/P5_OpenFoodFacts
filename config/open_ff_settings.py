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
"page_size" : "1",
"page" : "1",
"json" : "1"
}

#User choise
categories=["Viande","Plats préparés","Boissons","Petit_déjeunés","Fromages"]

# Desired food information:
fr_food_informations = { "Non du produit" : "product_name", "Nom générique" : "generic_name",\
     "Marques" : "brands", "Catégories" : "categories", "Note\n(A à E)" : "nutrition_grades",\
     "Classif.\nNova\n(1 à 4)" : "nova_groups", "Allergènes" : "allergens", 
          "Lien Open Food Facts" : "url", "Magasin" : "stores" }