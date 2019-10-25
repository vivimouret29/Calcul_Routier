#!C:\Users\BEP29\AppData\Local\Programs\Python\Python37-32\python.exe

import json
import requests

launch = True   #permet de relancer l'application

while launch == True:

    print("Programme de Calcul Routier")
    origins = input("Entrez la ville et le département de départ : ")
    destinations = input("Entrez la ville et le département d'arrivée : ")

    request = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?origins='+origins+'&destinations='+destinations+'&key=AIzaSyAeio9oOWJPUFFoDsN2mWMyXIU52ulRTzk')
    #utilisation API Google Distance Matrix

    result = json.loads(request.text)
    #conversion de la recherche en dictionnaire python

    distance = round(result['rows'][0]['elements'][0]['distance']['value'] / 1000)

    def temps():            #calcul le temps du trajet
        minutes = 0
        hours = 0
        dist = distance
        if dist > 180:
            while dist >= 180:
                dist -= 153
                minutes += 15
                hours += 2
        else:
            while dist > 1:
                dist -= 1.5
                minutes += 1
        if minutes >= 60:
            count = minutes
            count -= 60
            if 59 >= count >= 0:
                hours += 1
                minutes = count
            else:
                minutes = 0
                hours += 1
        return hours,minutes

    hours,minutes = temps()
    temps()

    #print(result)
    print("Vous avez " + str(distance) + " km à parcourir en "+str(hours)+"h "+str(minutes)+" minutes.")        #affichage des résultats
    if hours >= 3:
        print("Faites une pause de 15 minutes toutes les 2h pour votre sécurité.")

    choice = input("Voulez-vous relancer une recherche ? (o/n)")
    if choice not in ('o', 'oui'):
        launch = False