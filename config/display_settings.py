#! /usr/bin/python3
# -*-coding: utf-8-*-


# Text messages
messages = {
"Welcome" : "                                                           Bienvenu dans l'application Open Food Alernative !                                                  ",
"Category_choice" : "Veuillez saisir un numéro de categorie selon le choix proposé ('Q' ou 'q' pour quitter): ",
"Product_choice" : "Veuillez saisir le numéro d'index du produit que vous souhaiter substituer ('Q' ou 'q' pour quitter) : ",
"Pagination_info" : "Vous pouvez utiliser les entrées +/- pour faire défiler les pages ! "

}
# Text errors
errors = {
"ValueError" : " Votre entrée n'est pas valide, veuillez recommencer."
}

counter = "Vous avez {} résultat(s) pour votre requête."

# Variable to del the preview line (Error message )
del_preview_line = "\033[A"

# Colors choice for color the user interface
colours = {
	"default"    :    "\033[0m",
	# style
	"bold"       :    "\033[1m",
	"underline"  :    "\033[4m",
	"blink"      :    "\033[5m",
	"reverse"    :    "\033[7m",
	"concealed"  :    "\033[8m",
	# text colors
	"black"      :    "\033[30m",
	"red"        :    "\033[31m",
	"green"      :    "\033[32m",
	"yellow"     :    "\033[33m",
	"blue"       :    "\033[34m",
	"magenta"    :    "\033[35m",
	"cyan"       :    "\033[36m",
	"white"      :    "\033[37m",
	# background colors
	"on_black"   :    "\033[40m",
	"on_red"     :    "\033[41m",
	"on_green"   :    "\033[42m",
	"on_yellow"  :    "\033[43m",
	"on_blue"    :    "\033[44m",
	"on_magenta" :    "\033[45m",
	"on_cyan"    :    "\033[46m",
	"on_white"   :    "\033[47m"
    }
