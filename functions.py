import random
#liste des animaux
animals0 = ["Zèbre", "Bogey", "Mâle", "2,32m", "400kg"]
animals1 = ["Zèbre", "Jelly", "Femelle", "2,19m", "350kg"]
animals2 = ["Zèbre", "Lunar", "Femelle", "2,24m", "360kg"]
animals3 = ["Zèbre", "Stewy", "Femelle", "2,11m", "340kg"]
animals4 = ["Girafe", "Gazo", "Mâle", "4,5m", "1950kg"]
animals5 = ["Girafe", "Hazel", "Mâle", "4,3m", "1870kg"]
animals6 = ["Girafe", "Hubble", "Femelle", "3,8m", "1230kg"]
animals7 = ["Lion", "Cedar", "Mâle", "2,5m", "230kg"]
animals8 = ["Lion", "Geneva", "Femelle", "1,6m", "180kg"]

enclosureOne = [animals0, animals1, animals2, animals3]
enclosureTwo = [animals4, animals5, animals6]
enclosureThree = [animals7, animals8]

zoo = [enclosureOne, enclosureTwo, enclosureThree]
animalsQuantitys = len(enclosureOne) + len(enclosureTwo) + len(enclosureThree)

# Affichage des animaux
def displayAnimal():
    for i in range(len(zoo)):
        for j in range(len(zoo[i])):
            espece = zoo[i][j][0]
            nom = zoo[i][j][1]
            sexe = zoo[i][j][2]
            taille = zoo[i][j][3]
            poids = zoo[i][j][4]
            print("Un(e)",espece,sexe,"qui mesure",taille,"et pèse",poids, "et qui s'appelle",nom)

#ajout d'un animal
def addAnimal(liste):
    espece = input("Quelle est l'espèce de l'animal ? ")
    nom = input("Quel est le nom de l'animal ? ")
    sexe = input("Quel est le sexe de l'animal ? ")
    taille = input("Quelle est la taille de l'animal ? ")
    poids = input("Quel est le poids de l'animal ? ")
    addAnimal.append(liste) = [espece, nom, sexe, taille, poids]
    print("Dans quel enclos voulez-vous ajouter l'animal ?")
    print("1 - Enclos 1 (Zèbres)")
    print("2 - Enclos 2 (Girafes)")
    print("3 - Enclos 3 (Lions)")
    choiceEnclosure = input("Votre choix ? ")
    match choiceEnclosure:
        case "1":
            enclosureOne.append(addAnimal)
            print("L'animal a été ajouté dans l'enclos 1.")
        case "2":
            enclosureTwo.append(addAnimal)
            print("L'animal a été ajouté dans l'enclos 2.")
        case "3":
            enclosureThree.append(addAnimal)
            print("L'animal a été ajouté dans l'enclos 3.")
        case _:
            print("Choix invalide. L'animal n'a pas été ajouté.")

#retirer un animal
def removeAnimal(liste):
    nom = input("Quel est le nom de l'animal à retirer ? ")
    for i in range(len(liste)):
        if liste[i][1] == nom:
            liste.pop(i)
            print("L'animal", nom, "a été retiré.")
            return
    print("Aucun animal trouvé avec le nom", nom)

#remplacer un animal
def replaceAnimal(liste):
    nom = input("Quel est le nom de l'animal à remplacer ? ")
    for i in range(len(liste)):
        if liste[i][1] == nom:
            print("Entrez les informations du nouvel animal :")
            espece = input("Espèce : ")
            newNom = input("Nom : ")
            sexe = input("Sexe : ")
            taille = input("Taille : ")
            poids = input("Poids : ")
            liste[i] = [espece, newNom, sexe, taille, poids]
            print("L'animal", nom, "a été remplacé par", newNom)
            return
    print("Aucun animal trouvé avec le nom", nom)

# Affichage du personnel
def displayEmployees(healerQuantity, vetQuantity, cleanerQuantity):
    print(healerQuantity, "soigneurs")
    print(vetQuantity, "vétérinaire")
    print(cleanerQuantity, "agent d'entretien")


# Simuler une journée
def simulateDay(dayCost, entranceFee, hostelPrice, cashInitial):
    # Demande du nombre de visisteur
    visitorQuantity = random.randint(100, 250)
    print(str(visitorQuantity) + " visiteurs arrivent pour voir les animaux.")
    visitorHostel = random.randint(10, 100)
    # Nombre de visiteurs ayant quitté le zoo
    visitorLeft = int(visitorQuantity) - int(visitorHostel)
    print(str(visitorHostel) + " visiteurs dorment à l'hôtel.")
    print(str(visitorLeft) + " visiteurs ont quitté le Zoo.")
    # Calcul de la trésorerie
    cash = cashInitial - dayCost
    cash = cash + (entranceFee * int(visitorQuantity))
    cash = cash + (hostelPrice * int(visitorHostel))
    visitorCash = (cash - cashInitial) / int(visitorQuantity)
    print("Recette : " + str(cash - cashInitial) + " €")
    cashInitial = cash
    print("Trésorerie : " + str(cash) + " €")
    print("Gain moyen par visiteur : " + str(visitorCash) + " €")
    return cashInitial