#Importation de la biliothèque OS
import os

#Importation de la bibliothèque TIME
import time

#Importation de la bibliothèque des couleurs
from colorama import init
init()
from colorama import Fore






#Supprimer l'intégralité de la console
os.system("clear")


#Afficher le logo de Vuizion en ASCII ART en couleur cyan
print(Fore.CYAN)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@             @@@@")
print("@@@@@@@@  @@@@@@@@@@@@@@@@")
print("@@@@@@@  @@ @@@@ @@@ @@@@@")
print("@@@  @@  @@ @@@@ @@@ @@@@@")
print("@@@@  @ =@@ @@@@ @@@ @@@@@")
print("@@@@@ @ @@@ @@@@ @@@ @@@@@")
print("@@@@@   @@@ @@@@ @@@ @@@@@")
print("@@@@@@  @@@@    @@@@ @@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@")
print(Fore.RESET)








###########################################
################ FONCTIONS ################
###########################################



################
## Calculer la racine d'une équation du premier degrés
################

def prem_deg():
    print("")
    print("-----------------------")
    print("")


    #On affiche le type d'équation que l'utilisateur à choisi
    print("Vous avez choisi : " + Fore.LIGHTGREEN_EX + "ÉQUATION DU PREMIER DEGRÉS" + Fore.RESET)


    #On donne un exemple d'équation
    print("Pour résoudre une équation du type '" + Fore.LIGHTYELLOW_EX + "a" + Fore.RESET + "x + " + Fore.LIGHTYELLOW_EX + "b" + Fore.RESET + " = 0'")
    print("")


    #On demande à l'utilisateur la valeur des lettres
    a = float(input("> Indiquez la valeur de '" + Fore.LIGHTYELLOW_EX + "a" + Fore.RESET + "' : "))
    print("")
    b = float(input("> Indiquez maintenant la valeur de '" + Fore.LIGHTYELLOW_EX + "b" + Fore.RESET + "' : "))

    print("")
    print("-----------------------")
    print("")


    #On montre à l'utilisateur l'équation qui va être résolue
    print("L'équation à résoudre est '" + Fore.LIGHTYELLOW_EX + str(a) + Fore.RESET + "x + " + Fore.LIGHTYELLOW_EX + str(b) + Fore.RESET + " = 0'.")
    print("")


    #Résolution de l'équation par calcul
    x = -b/a


    #On affiche le résultat dans la console
    print("Le résultat est " + Fore.LIGHTGREEN_EX + "x = " + str(x) + Fore.RESET)
    print("")








################
## Calculer la ou les racines d'une équation du deuxième degrés
################

def deux_deg():
    print("")
    print("-----------------------")
    print("")


    #On affiche le type d'équation que l'utilisateur à choisi
    print("Vous avez choisi : " + Fore.LIGHTMAGENTA_EX + "ÉQUATION DU SECOND DEGRÉS" + Fore.RESET)


    #On donne un exemple d'équation
    print("Pour résoudre une équation du type '" + Fore.LIGHTYELLOW_EX + "a" + Fore.RESET + "x² + " + Fore.LIGHTYELLOW_EX + "b" + Fore.RESET + "x + " + Fore.LIGHTYELLOW_EX + "c" + Fore.RESET + " = 0'")
    print("")


    #On demande à l'utilisateur la valeur des lettres
    a = float(input("> Indiquez la valeur de '" + Fore.LIGHTYELLOW_EX + "a" + Fore.RESET + "' : "))
    print("")
    b = float(input("> Indiquez maintenant la valeur de '" + Fore.LIGHTYELLOW_EX + "b" + Fore.RESET + "' : "))
    print("")
    c = float(input("> Puis indiquez la valeur de '" + Fore.LIGHTYELLOW_EX + "c" + Fore.RESET + "' : "))


    print("")
    print("-----------------------")
    print("")


    #On montre à l'utilisateur l'équation qui va être résolue
    print("L'équation à résoudre est '" + Fore.LIGHTYELLOW_EX + str(a) + Fore.RESET + "x² + " + Fore.LIGHTYELLOW_EX + str(b) + Fore.RESET + "x + " + Fore.LIGHTYELLOW_EX + str(c) + Fore.RESET + " = 0'.")
    print("")



    #Résolution de l'équation par calcul
    delta = b*b-4*a*c

    #On affiche la valeur du discrimiant
    print("La valeur du discriminant est " + Fore.LIGHTGREEN_EX + "Δ = " + str(delta) + Fore.RESET)



    if delta > 0 :
        #On calcul la seul racine de l'équation
        x1 = (-b-delta**0.5)/(2*a)
        x2 = (-b+delta**0.5)/(2*a)

        #On affiche le résultat dans la console
        print("L'équation possède alors deux solutions ;")
        print("Donc " + Fore.LIGHTGREEN_EX + "x1 = " + str(x1) + Fore.RESET + " et "+ Fore.LIGHTGREEN_EX + "x2 = " + str(x2) + Fore.RESET)
        print("")


    elif delta == 0 :
        #On calcul la seul racine de l'équation
        x0 = -b/(2*a)

        #On affiche le résultat dans la console
        print("Donc " + Fore.LIGHTGREEN_EX + "x0 = " + str(x0) + Fore.RESET + " est la solution de l'équation.")
        print("")


    else :
        #Puisque le discriminant est négatif, aucune racine n'est possible
        print("L'équation n'a aucune solution puisque le discrimiant est négatif.")
        print("")








################
## Résolution par la méthode balayage
################

def meth_bal():
    #TODO: Faire le code pour balayage
    print("")
    print("-----------------------")
    print("")


    #On affiche le type d'équation que l'utilisateur à choisi
    print("Vous avez choisi : " + Fore.LIGHTBLUE_EX + "MÉTHODE PAR BALAYAGE" + Fore.RESET)


    #On donne un exemple d'équation
    print("Pour résoudre une équation du type '" + Fore.LIGHTYELLOW_EX + "a" + Fore.RESET + "x² + " + Fore.LIGHTYELLOW_EX + "b" + Fore.RESET + "x + " + Fore.LIGHTYELLOW_EX + "c" + Fore.RESET + " = 0'")
    print("")


    #On demande à l'utilisateur la valeur des lettres
    a = float(input("> Indiquez la valeur de '" + Fore.LIGHTYELLOW_EX + "a" + Fore.RESET + "' : "))
    print("")
    b = float(input("> Indiquez maintenant la valeur de '" + Fore.LIGHTYELLOW_EX + "b" + Fore.RESET + "' : "))
    print("")
    c = float(input("> Puis indiquez la valeur de '" + Fore.LIGHTYELLOW_EX + "c" + Fore.RESET + "' : "))


    print("")
    print("-----------------------")
    print("")


    #On montre à l'utilisateur l'équation qui va être résolue
    print("L'équation à résoudre est '" + Fore.LIGHTYELLOW_EX + str(a) + Fore.RESET + "x² + " + Fore.LIGHTYELLOW_EX + str(b) + Fore.RESET + "x + " + Fore.LIGHTYELLOW_EX + str(c) + Fore.RESET + " = 0'.")
    print("")


    #On affiche toute les valeur de f(1) à f(8)
    x=0
    y=-1
    add_to_x = float(1)

    while add_to_x > 0.0001:
        while y < 0:
            x = round(x + add_to_x, 3)
            y = a*x*x + b*x + c
        borne_min = round(x-add_to_x, 3)
        borne_max = x
        x = x-add_to_x
        y = -1
        add_to_x = add_to_x/10
    print("Le résultat se trouve dans l'intervale [" + Fore.LIGHTBLUE_EX + str(borne_min) + ";" + str(borne_max) + Fore.RESET + "] avec ")
    print("")








###########################################
############## DEBUT DU CODE ##############
###########################################

print("")
print("-----------------------")
print("")
print("Bienvenue dans Vuizion Solver !")
print("")
print("-----------------------")
print("")

#Demande à l'utilisateur quelle équation utiliser

print("Veuillez choisir le type d'équation svp :")
print(Fore.LIGHTGREEN_EX + "1 : Équation du premier degrés" + Fore.RESET)
print(Fore.LIGHTMAGENTA_EX + "2 : Équation du second degrés" + Fore.RESET)
print(Fore.LIGHTBLUE_EX + "3 : Équation résolue par méthode balayage" + Fore.RESET)
print("")






################
## Menu de choix pour l'utilisateur
################

i=1
while i==1 :
    #Changer le message d'erreur lorsqu'il ne s'agit pas d'un nombre entier
    while i==1:
        try:
            choice = int(input("> Entrez le numéro correspondant : "))
            break
        except ValueError:
            print(Fore.LIGHTRED_EX + "Désolé, vous devez entrer un nombre entier préenregistré. Veuillez réessayer." + Fore.RESET)
            print("")
            i=1

    #Si l'utilisateur choisi une équation du premier degrés, exécuter la fonction "prem_deg"
    if choice == 1:
        prem_deg()
        i=0

    #Si l'utilisateur choisi une équation du deuxième degrés, exécuter la fonction "deux_deg"
    elif choice == 2:
        deux_deg()
        i=0

    #Si l'utilisateur choisi une équation du deuxième degrés, exécuter la fonction "deux_deg"
    elif choice == 3:
        meth_bal()
        i=0

    #Si l'utilisateur ne choisi pas un réponse préenregistrée, l'erreur lui est communiquée
    else:
        print(Fore.LIGHTRED_EX + "Désolé, vous devez entrer un nombre préenregistré. Veuillez réessayer." + Fore.RESET)
        print("")
        i=1