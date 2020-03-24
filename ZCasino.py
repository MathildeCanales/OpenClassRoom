from math import ceil
from random import randrange


def faire_un_pari():
    mise = -10 # 1. mise = -10
    while mise>budget or mise<0: # 2. -10 inferieur a 0 = condition est vrai 7. idem 2

        mise_saisie = input("quelle est votre mise ?  ") # 3. mise = -10 mise_saisi = toto 8. mise_saisi = 12

        try:
            mise=int(mise_saisie) # 4. raise ValueError 9. mise = 12
            if mise>budget or mise<0: # 13.
                print("Merci d'entrer une mise entre 0 et votre cagnotte. Votre cagnotte est de :",budget)
        except ValueError:
            print("Mauvaise valeur, recommencez") # 5. mise = -10 mise_saisi = toto


    chiffre=-10
    while chiffre>49 or chiffre<0:
        
        chiffre_saisie=input("Sur quel chiffre souhaitez-vous miser ? (compris entre 0 et 49 inclus)  ")

        try: 
            chiffre=int(chiffre_saisie) 
            if chiffre>49 or chiffre<0:
                print("Merci d'entrer un chiffrer entre 0 et 49 inclus.")
        except ValueError:
            print("Mauvaise valeur, recommencez")
    
    return mise,chiffre


def roulette():
    resultat=randrange(50)
    print("Le numéro gagnant est.......... LE NUMERO....",resultat,"!")
    return resultat

def calcul_gain(budget, chiffre, resultat):
    gain=0
    if resultat==chiffre:
        gain=4*mise
        budget=budget+gain
        print("BRAVO ! Vous remportez ",gain,". Votre cagnotte est désormais de : ",budget)
    elif resultat%2==1 and chiffre%2==1:
        gain=ceil(1.5*mise)
        budget=budget+gain
        print("BRAVO ! Le numéro gagnant est impair, comme votre chiffre. Vous remportez ",gain,". Votre cagnotte est désormais de : ", budget)
    elif resultat%2==0 and chiffre%2==0:
        gain=ceil(1.5*mise)
        budget=budget+gain
        print("BRAVO ! Le numéro gagnant est pair, comme votre chiffre. Vous remportez ",gain,". Votre cagnotte est désormais de : ", budget)
    else:
        budget=budget-mise
        print("Pas de chance ! Vous avez perdu ! Votre cagnotte est désormais de ", budget)
    return gain,budget



budget = 100
while budget>0:
    mise,chiffre=faire_un_pari()
    resultat=roulette() 
    gain,budget=calcul_gain(budget, chiffre, resultat)