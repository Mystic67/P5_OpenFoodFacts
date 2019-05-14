L'application est en mode console et interagit avec la base de données Open Food Facts. Elle permet à l'utilisateur de rechercher un aliment de substitution plus sains à un aliment de son choix. L'utilisateur a alors la possibilité d'enregistrer le produit choisi et son substitut dans sa base de données locale. Il sera en mesure de consulter les aliments enregistrés avec les alternatives correspondantes.  


Spécifications fonctionnelles:

Au démarrage, l'application créé la base de données et les tables, puis affiche le menu principal pour demander un choix utilisateur.
    1. Mettre à jour la base de données.
    2. Rechercher un aliment de substitution
    3. Voir mes aliments de substitution favoris.
    ---------------------------------------------------------------------------
    1.1 Le système se connecte à OpenFoodFacts les données pour chaque catégorie défini et stock les informations dans la base de données locale.
    ---------------------------------------------------------------------------
    2.1 Le système affiche un tableau avec la liste des catégories d'aliments disponible et demande à l'utilisateur de saisir l'index de la catégorie de son choix.
    2.2 L'utilisateur saisi le numéro d'index de la catégorie souhaitée.
    2.3 Le système affiche à l'utilisateur un tableau avec la liste des aliments de la catégorie choisie. L'utilisateur est invité à saisir l'aliment pour lequel il souhaite trouver un produit de substitution.
    2.4 L'utilisateur saisi l'index de son choix.
    2.5 Le système recherche dans la base de données locale les produits de substitution plus sains ou selon l'indice de notation du produit. Il affiche à l'utilisateur le produit sélectionné et la liste de des substituts potentiels de la même catégorie. Une nouvelle fois, l'utilisateur est inviter à entrer le numéro d'index d'un aliment de substitution pour visualiser les détails et comparer avec le produit initial.
    2.6 L'utilisateur saisi un index.
    2.7 Le système affiche affiche un tableau à deux colonnes permettant à l'utilisateur d'effectuer une comparaison entre les deux aliments. Le système propose à l'utilisateur d'enregistrer le tableau comparatif entre l'aliment et son substitut dans ses favoris.
    2.8 L'utilisateur demande l'enregistrement par la saisie de la réponse 'Oui'.  
    2.7 Le système enregistre le comparatif entre le produit et son substitut dans la base de données locale, puis reviens au menu principal.
    ---------------------------------------------------------------------------
    3.1 Le système affiche le tableau comparatif entre les produits et leurs substituts enregistrés dans dans les favorites. L'utilisateur peut naviger dans les pages en saisissant les entrée +/-.

    NB: L'utilisateur à la possibilité à chaque étape de saisie, de revenir au menu principal et depuis le menu principal, de quitter l'application.
