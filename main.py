import functions

# Informations personnel
healerQuantity = 2
veterinaryQuantity = 1
cleanerQuantity = 1

# Information pour trésorerie
dayCosts = 2000
entranceFee = 5
hostelPrice = 50
cashInitial = 200000

# Jour semaine
nbJour = 1

isContinue = True
while isContinue:
    # Menu
    print("=================================================================")
    print("Jour " + str(nbJour))
    print("1 - Afficher les animaux")
    print("2 - Afficher le personnel")
    print("3 - Simuler une journée")
    print("4 - Ajouter un animal")
    print("5 - Retirer un animal")
    print("6 - Remplacer un animal")
    print("fin - Quitter")
    choice = input("Votre choix ?")
    print("=================================================================")
    match choice:
        case "1":
            print(len(functions.enclosureOne), 'animaux dans l\'enclos 1')
            print(len(functions.enclosureTwo), 'animaux dans l\'enclos 2')
            print(len(functions.enclosureThree), 'animaux dans l\'enclos 3')
            print(len(functions.animalsQuantitys), 'animaux totaux dans le zoo')
            functions.displayAnimal()

        case "2":
            functions.displayEmployees(healerQuantity, veterinaryQuantity, cleanerQuantity)
        case "3":
            cashInitial = functions.simulateDay(
                dayCosts, entranceFee, hostelPrice, cashInitial
            )
            nbJour += 1
        case "4":
            functions.addAnimal()
        case "5":
            functions.removeAnimal()
        case "6":
            functions.replaceAnimal()
        case "fin":
            isContinue = False
            print("Fin du programme")

        case _:
            print("Merci de saisir un nombre entre 1 et 3 inclus ou fin")