import time

name = "animals"
nb = int(0)
taille = float(0)

name2 = "zèbre"
taille2 = float(1.40)
nb2 = int(2)

vault = 200000
ticket = 5
night = 50
cost = 2000

moyguest = 0

day = "lundi"

name = str(input("Indiquez le nom de/des l'animal/aux: "))
nb = int(input("Combient y aura t'il d'animal/animaux:"))
if nb == 1:
    taille = float(input("Indiquez sa taille: "))
elif nb < 1:
    print("ALORS LA ! les ", name, " ils vont être nombreux ! \n T'es sur ça rentre même ?\n #LABLAGUE #ILESTSEUL #REMYSANSAMI #RATIO #J'AIFINI")
else:
    taille = float(input("Indiquez la taille moyennes des animaux:"))

if taille < 0.2 :
    print("\n IL EST BAAAAD PETIT\n")
    time.sleep(2)

if taille >= 4 :
    print("\nIL EST BAAAAD GRAND\n")
    time.sleep(2)

print("Vous allez accueillir", nb, name,"de", taille,"m en moyenne.")

time.sleep(2)

print("Un an plus tard.")
nb = nb * 3
print("Vos animaux ont triplé, il y en à maintenant", nb, name, "et 2 zèbres sont arrivés.")

time.sleep(1)

print("Vous avez maintenant dans vote ZOO.")
print(nb + nb2, "animaux")
print(nb, name,"qui mesurent en moyenne", taille, "m.")
print(nb2, name2, "qui mesurent en moyenne", taille2, "m.")

time.sleep(1)

print("Vous avez maintenant ouvert votre zoo au public.")
guest = int(input("Combien de visiteurs vont-ils entrés dans votre ZOO ?: "))

if guest <= 2:
    print("CIEEEEL, TU M'AVAIS PAS DIS QUE TON ZOO IL FLOPAIS !\n #GIMS")
print("Il y à", guest, "visiteurs, dans votre ZOO.")

time.sleep(1)

hotel = int(input("Combien de visiteurs reste dormir à l'hotel du ZOO ?: "))
if hotel == 0:
    print("LE FOP ULTIME")

if hotel > guest:
    print("Bon. La c'est grave. J'abandonne.")
else :
    print("Il y à ",hotel, "qui sont restés dormir à l'hotel.")
    print("et", guest - hotel, "Qui sont partis du ZOO.")

    time.sleep(2)

    nightbenef = hotel*night
    ticketbenef = ticket*guest

    print("Ajourd'hui le ZOO, aura générer", ticketbenef + nightbenef, "€ Pour un gain total de", ticketbenef+nightbenef-cost, "€ sur la trésorire qui était à:", vault," €")
    moyguest = (ticketbenef + nightbenef - cost)/guest
    print("Soit un gain moyen de ", moyguest, " € par visiteurs.")
    if moyguest == 0:
        print("Au moins t'as rien perdu.")
    if moyguest < 0:
        print("T'es dans la merde, la.")

    ### PARTIE 2 ###

    ## Menu de séléction
    daycount = 1
    simvault = 20000

    def menu():
        global daycount
        global simvault

        print("Jour : ", daycount)
        print("Choix 1: Afficher tous les animaux du ZOO.\nChoix 2: Afficher le personnel.\nChoix 3: Simuler une journée.\nChoix 4: Simuler la trésorerie sur une période\n fin - Quitter")
        choice = input("Qu'elle choix voulez vous faire ? (1, 2, 3, 4 ou fin) ")

        match choice :
            case str("1") :
                print(animals)
                menu()
            case str("2") :
                print(staff)
                menu()
            case str("3") :
                simcost = 2000
                simguest = 1
                simhotel = 1
                simticket = 5
                simnight = 50

                simticketbenef = simguest * simticket
                simhotelbenef = simhotel * simnight

                simmoybenef = (simticketbenef + simhotelbenef - simcost) / simguest

                simguest = int(input("Combient de visiteur, viennent au ZOO ?"))
                print(int(simguest), " visiteurs viennent pour admirer vos animaux")

                simhotel = int(input("Combient reste dormir à l'hotel ?"))
                simvault = simvault - simcost + simticketbenef + simhotelbenef
                print(int(simhotel), " visiteurs reste à l'hotel.\n", (simguest - simhotel), " ont quittés le ZOO.\n Il vous reste dans la trésorerie: ", (simvault), "\n Soit un gain moyen par visiteur de: ", float(simmoybenef))
                daycount = daycount + 1
                menu()
            case str("4") :
                simdayvault2 = int(input("Combient de jour voulez vous simuler ?"))
                simvault2 = 20000
                for i in range(simdayvault2):
                    simcost2 = 2000
                    simguest2 = 1
                    simhotel2 = 1
                    simticket2 = 5
                    simnight2 = 50


                    simguest2 = int(input("Combient de visiteur, viennent au ZOO ?"))
                    print(int(simguest2), " visiteurs viennent pour admirer vos animaux")

                    simhotel2 = int(input("Combient reste dormir à l'hotel ?"))
                    
                    simticketbenef2 = simguest2 * simticket2
                    simhotelbenef2 = simhotel2 * simnight2
                    simmoybenef2 = (simticketbenef2 + simhotelbenef2 - simcost2) / simguest2
                    simvault2 = simvault2 - simcost2 + simticketbenef2 + simhotelbenef2

                print('Après', simdayvault2, 'jours de simulation:')
                print("Il vous reste dans la trésorerie: ", (simvault2), "\n Soit un gain moyen par visiteur de: ", float(simmoybenef2))
            case "fin":
                print("Passez une bonne journée !")

            case _ :
                print("Vous ne pouvez faire que 5 Choix. \nUn choix c'est un numéro ou fin à saisir, tu peux en faire 5. Donc soit 1, 2, 3, 4 ou fin. \nC'est pas dur, pourtant. Et je suis la à te demander alors que je m'en fou complétement, \n\nTu veux pas être normal deux secondes et réfléchir, un peu. \n\nJE SUIS UN PROGRAMME. ET TOI TA UN CERVEAU QUI TE SERT A RIEN !")
                menu()
                return

    day = str(input("Qu'elle jour est-il ? (lundi, mardi...) "))
    print("Nous sommes le ",day, ".")
    
    if str(day) == "dimanche":
        print("Le ZOO est fermé")
    elif str(day) == "mardi":
        print("Le ZOO est fermé")
    else:
        choice = 0
        staff = "Voici les Staff du Zoo : \n 2 Soignants \n 1 vétérinaire \n 1 agent d'entretien"
        animals = "Voici Tous les animaux du ZOO, \nVous avez : \n"+" "+ str(nb) + " " + name + " " + "\nAinsi que" + " " + str(nb2) + " " +name2

        time.sleep(2)
        menu()