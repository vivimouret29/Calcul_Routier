# Programme Calcul Routier

## Projet : Programme calcul routier


### Énoncé :

Je suis un directeur d’entreprise de livraison routier à travers la France.

Écrire un programme qui affiche un tableau me permettant de connaître l'heure à laquelle une
livraison sera effectuée.

* Un camion accélère de 10 km/h, par minute.
* Un camion ralenti de 10 km/h, par minute.

Sa vitesse maximale est de 90 km/h.

Un conducteur doit faire une pause de 15 min toutes les 2 heures.

* Consignes :
    * l’exercice est à faire seul
    * vous avez le choix du langage
    * la date de rendu est le Vendredi 25 octobre 2019 23h59
    * le rendu se fera sur un dépôt Gitlab ou Github et vous déposerez le lien du dépôt sur Moodle

* Écrire un programme qui :
    * demande une ville de départ et une ville d’arrivée
    * retourne un tableau avec :
    * le nom de la ville de départ
    * le nom de la ville d’arrivée
    * la distance parcourue
    * le temps pour parcourir cette distance HH/mm (arrondi à la minute supérieure)

## Pour lancer le programme Python

Mon **Programme de Calcul Routier** est un fichier Python.

En utilisant l'`API Google Distance Matrix`, je reçois ma distance entre les deux villes.
Cela exige une connection internet haut-débit.

Suite à un algorithme, j'en déduis le temps de trajet du camion.

* Pour pourvoir utiliser le Programme de Calcul Routier, vous pouvez :
    * directement lancer le fichier avec le lanceur Python3.7
    * le lancer via votre terminal Windows, Linux et Mac

Veillez à **rentrer la région**, pour une recherche optimale.

*Ex : Entrez la ville de départ : Bordeaux,Nouvelle-Aquitaine*

Ressource distance entre deux villes :
https://www.bonnesroutes.com/mileage-chart/c2202162-france/