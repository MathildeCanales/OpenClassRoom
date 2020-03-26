lechenilbleu=[("Hector",7),("Vodka",2),("Moussaka",10),("Fluffy",30),("Max",7)] # list(tuple(nom du chien, du nombre de jour))

def afficher_chiens(lechenilbleu):
    i=0
    while i<len(lechenilbleu):
        chien = lechenilbleu[i] # chien est une variable de type tuple(nom du chien, du nombre de jour)
        print(chien[0])
        i = i + 1

def disponibilite(lechenilbleu):
    prochain_jour_dispo=("",365)
    i=0
    while i<len(lechenilbleu):
        if lechenilbleu[i][1]<prochain_jour_dispo[1]:
            prochain_jour_dispo=lechenilbleu[i]
        i=i+1
    print("Nom d'un chien ! Le chenil bleu est complet. La prochaine disponibilité est dans",prochain_jour_dispo[1]+1,"jours !")

def nouveau_chien(lechenilbleu):
    capacite_chenil=6
    if len(lechenilbleu)<capacite_chenil:
        nom_chien = input("Comment s'appelle le nouvel entrant ?")
        duree_sejour=input("Combien de jours reste t-il au chenil?")
        duree_sejour=int(duree_sejour)
        lechenilbleu.insert(len(lechenilbleu)+1,(nom_chien,duree_sejour))
        afficher_chiens(lechenilbleu)
    else : 
        disponibilite(lechenilbleu) 

