L'application est en mode console et interagit avec la base de donnée Open Food Facts. Elle permet à l'utilisateur de rechercher un aliment de substitution plus sain à un aliment de son choix. L'utilisateur à alors la possibilité d'enregistrer le produit choisi et son substitut dans sa base de données local. Il sera en mesure de consulter les aliments enregistrer avec les alternatives correspondantes.  


Spécifications fonctionnelles:

Au démarrage, l'application affiche le menu pour demander un choix utilisateur.
    1. Rechercher un aliment de substitution
    2. Afficher mes produits de substitution enregistrés.

    1.1 Le système affiche un tableau avec la liste des catégories d'aliments disponible et 			demande à l'utilisateur de saisir l'index de la catégorie de son choix.
    1.2 L'utilisateur saisi le numéro d'index de la catégorie souhaitée.
    1.3 Le système se connecte à la base de données d'OpenFoodFacts, récupère les produits de 		la catégorie choisi, stock les information dans la base de données local, et affiche à 			l'utilisateur un tableau avec la liste des aliments de la catégorie choisi. L'utilisateur est 			invité à saisir l'aliment pour lequel il souhaite trouver un produit de substitution.
    1.4 L'utilisateur saisi l'index de son choix.
    1.5 Le système recherche dans la base de données local les produits de substitution plus sain 		ou au moins équivalent si l'indice de notation du produit est déjà bas. Il affiche à 			l'utilisateur le produit sélectionné et la liste de ses substituts. Une nouvelle fois, l'utilisateur 	est inviter à entrer le numéro d'index d'un aliment de substitution s'il souhaite l'enregistrer 		dans sa base de données.
    1.6 L'utilisateur saisi un index.
    1.7 Le système enregistre le produit et son substitution choisis dans la base de données local, 		puis reviens au menu principal à l'étape 1.1

    2.1 Le système affiche la liste des produits et leurs substituts enregistré dans la base de 			données. L'utilisateur peut saisi l'index d'un produit de substitution qu'il souhaite 			supprimer de sa base de données ou de supprimer intégralement les produits enregistrés. 		Le système demande confirmation si une suppression est demandé et reviens au menu 			principal.

    NB: L'utilisateur à la possibilité à chaque étape de saisi, de revenir au menu principal et depuis 		le menu principal, de quitter l'application.
