########################### Description #######################################

L'application est en mode console et utilise les données de la base de données Open Food Facts. Elle permet à l'utilisateur de rechercher un aliment de substitution plus sains à un aliment de son choix. L'utilisateur a la possibilité d'enregistrer le produit choisi avec son substitut dans sa base de données locale. Il sera en mesure de consulter les aliments et leurs substituts enregistrés .  


####################### Spécifications fonctionnelles: ########################

Au démarrage, l'application créé la base de données et les tables, puis affiche le menu principal pour demander un choix utilisateur.

1. Mettre à jour la base de données.
2. Rechercher un aliment de substitution
3. Voir mes aliments de substitution favoris.


    ########################### Choix 1. ######################################

    1.1 Le système se connecte à OpenFoodFacts, récupère les données pour chaque catégorie définie dans open_ff_settings.py et stock les informations dans la base de données locale.

    ############################ Choix 2. #####################################

    2.1 Le système affiche un tableau avec la liste des catégories d'aliments disponible et demande à l'utilisateur de saisir l'index de la catégorie de son choix.
    2.2 L'utilisateur saisi le numéro d'index de la catégorie souhaitée.
    2.3 Le système affiche à l'utilisateur un tableau avec la liste des aliments de la catégorie choisie. L'utilisateur est invité à saisir l'aliment pour lequel il souhaite trouver un produit de substitution.
    2.4 L'utilisateur saisi l'index de son choix.
    2.5 Le système recherche dans la base de données locale les produits de substitution plus sains ou selon l'indice de notation du produit. Il affiche à l'utilisateur le produit sélectionné et la liste des substituts potentiels de la même catégorie. Une nouvelle fois, l'utilisateur est inviter à entrer le numéro d'index d'un aliment de substitution pour visualiser les détails et comparer avec le produit à substituer.
    2.6 L'utilisateur saisi un numéro d'index.
    2.7 Le système affiche un tableau à deux colonnes permettant à l'utilisateur d'effectuer une comparaison entre les deux aliments. Le système propose à l'utilisateur d'enregistrer le tableau comparatif entre l'aliment et son substitut dans ses favoris.
    2.8 L'utilisateur demande l'enregistrement par la saisie de la réponse 'Oui'.  
    2.7 Le système enregistre le comparatif entre le produit et son substitut dans la base de données locale, puis reviens au menu principal.


    ############################## Choix 3. ###################################

    3.1 Le système affiche le tableau comparatif entre les produits et leurs substituts enregistrés dans dans les favorites. L'utilisateur peut naviger dans les pages en saisissant les entrée +/-.

    NB: L'utilisateur à la possibilité à chaque étape de saisie, de revenir au menu principal et depuis le menu principal, de quitter l'application.


############################### INSTALLATION ##################################

    # OpenFoodAlternative
Openclassrooms Project_5 en Python3

### Installer le seveur de base de données MySQL:
Pour utiliser  cette application il est nécessaire d'installer un serveur de base de données MySQL, puis, de définir un nom d'utilisateur ainsi que les privilèges sur votre base de données.
exemple de commande dans la console MySQL pour créer un utilisateur:
- CREATE USER 'nom_utilisateur'@'adresse_IP_de_mon_serveur' IDENTIFIED BY 'mon_mot_de_passe'

exemple de commande dans la console MySQL pour accorder tous les privilèges sur votre base de données à un utilisateur:
- GRANT ALL PRIVILEGES ON mabase_de_donnees.* TO 'nom_utilisateur'@'adresse_IP_de_mon_serveur';

Vous devez ensuite remplacer les valeur d'accès par défaut à la base de données par vos valeurs personnalisées dans le fichier config/open_ff_settings.py :

SERVER_ACCES = {
  'host': 'adresse_IP_de_mon_serveur',     # L'adresse de votre serveur
  'user': 'nom_utilisateur',               # Votre nom d'utilisateur
  'password': 'mot_de_passe'               # Votre mot de passe d'accès à la DB
}

DB_NAME = 'mabase_de_donnees'              # Le nom de votre base de données


### Installer de python3:
Voir page ci-dessous:
https://www.python.org/downloads/

Si vous avez besoin des droits administrateur "root", utiliser "sudo" en début de commande.
__________________________________________________________________________________________________________________________
### Installer pip3:
  ##### python3 -m pip
  ou
  ##### python -m pip (Windows with Python3 installed)
Voir page ci-dessous:
https://pip.pypa.io/en/stable/installing/
___________________________________________________________________________________________________________________________
### Installer un environnement virtuel Python3 pip3 comme vitual par exemple:
  ##### pip3 install virtualenv.

### Créer un environment comme par exemple:
  ##### virtualenv env

### Activer l'environnement virtuel avec une commande comme par exemple:
  ##### source env/bin/activate
  ou
  ##### env\scripts\activate (Windows)
Voir page ci-dessous:
https://virtualenv.pypa.io/en/latest/installation/
____________________________________________________________________________________________________________________________
### Cloner ou télécharger l'application depuis GitHub dans le répertoire de votre environnement virtual:
  ##### https://github.com/Mystic67/P5_OpenFoodFacts

### Installer les requirements avec pip3 ou pip:
  ##### pip3 install /path/to/requirements.txt   
  (example: pip3 install /P5_OpenFooFacts/requirements)

### rendez-vous au répertoire P5_OpenFooFacts avec une commande comme:
  ##### cd /path/to/P5_OpenFooFacts/
  ou
  ##### cd \path\to\P5_OpenFooFacts\   (Windows)

### démarrer l'application avec une des commandes:
  ##### python3 open_ff_app.py
  ou
  ##### python open_ff_app.py (Windows with Python3 installed)
__________________________________________________________________________________________________________________________
