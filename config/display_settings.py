#! /usr/bin/python3
# -*-coding: utf-8-*-


main_choice_text = [
    "\tMettre à jour la base de données.\t",
    "\tRechercher un aliment de substitution\t",
    "\tVoir mes aliments de substitution favoris\t"]

# Text messages
messages = {
    "Welcome": "\t\t\t\t\t\t\t\tBienvenu dans l'application Open Foods Alternatives !\t\t\t\t\t\t\t\t\t\t",
    "Main_choice": "Veuillez saisir un numéro selon les choix proposés ('Q' ou 'q' pour quitter l'application): ",
    "Category_choice": "Veuillez saisir un numéro de categorie selon les choix proposés ('Q' ou 'q' pour revenir au menu principal): ",
    "Product_choice": "Veuillez saisir le numéro d'index de l'aliment que vous souhaiter substituer ('Q' ou 'q' pour revenir au menu principal) : ",
    "Substitute_choice": "Veuillez saisir le numéro d'index de l'aliment de substitition à comparer ('Q' ou 'q' pour revenir au menu principal) : ",
    "Save_substitute": "Souhaitez-vous enregistrer l'aliment et son substitut dans vos favoris ? ('Oui' pour enregistrer/ Q pour revenir au menu principal ) : ",
    "Pagination_info": "Vous pouvez utiliser les entrées +/- pour faire défiler les pages ! ",
    "Confim_saved": "Le produit N° {} et son substitut N° {} ont été enregistré dans vos favoris: ",
    "Favorites": "Veuillez saisir les entrées +/- ('Q' ou 'q' pour revenir au menu principal) : "}

# Text Menus
text_menus = {
    "Main_menu": "            Menu principal            ",
    "Category_choice": "          Choix de catégorie.         ",
    "Food_choice": "    Choix de l'aliment à substituer   ",
    "Substitute_choice": "  Choix d'un aliment de substitution  ",
    "product_comparison": "Comparatif des aliments / Enregistrement",
    "products_saved": " Mes aliments de substitution favoris ",
}

# Text errors
errors = {
    "ValueError": " Cette entrée n'est pas valide ! Veuillez recommencer.",
    "Save_error": " L'enregistrement dans la base de données à échoué !"
}

counter = "Vous avez {} résultat(s) pour votre requête."

separate_text = {
    "Main_question": "\tQue voulez-vous faire ?\t",
    "Product": "Aliment à substituer",
    "Substitute": "Aliment de substitution",

}

system_info = {
    "Api_Search": " Récupération des données d'OpenFoodFacts. Veuillez patienter !",
    "Table_update": " Mise à jour de la table '{}' de base de données. Veuillez patienter !",
    "Update_completed": " Mise à jour terminé ! "}

# Variable to del the preview line (Error message )
del_line = "\033[2K"
return_to_preview_line = "\033[A"

# Colors choice for color the user interface
colours = {
    "default": "\033[0m",
    # style
    "bold": "\033[1m",
    "underline": "\033[4m",
    "blink": "\033[5m",
    "reverse": "\033[7m",
    "concealed": "\033[8m",
    # text colors
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    # background colors
    "on_black": "\033[40m",
    "on_red": "\033[41m",
    "on_green": "\033[42m",
    "on_yellow": "\033[43m",
    "on_blue": "\033[44m",
    "on_magenta": "\033[45m",
    "on_cyan": "\033[46m",
    "on_white": "\033[47m"
}
