print("Bienvenue au Magashop! \nVous pouvez avoir des statistiques sur 1 semaine. Ou acheter ces articles disponibles à l'achat : \n- Un Stylo \n- Un Cahier \n- Une Cle USB")

sells1 = 0.0
sells2 = 0.0
sells3 = 0.0
nb1 = 0
nb2 = 0
nb3 = 0

stockstylo = 12
stockcahier = 8
stockusb = 5

def ventes():
    global sells, sells1, sells2, sells3, nb1, nb2, nb3, stockcahier, stockstylo, stockusb
    
    match sells:
        case 1:
            
            nb1 = int(input("Combien de stylos souhaitez-vous acheter ? "))
            if nb1 > stockstylo:
                print("Désolé, nous n'avons pas assez de stock pour cette quantité de stylos. Nous en avons que", stockstylo,"en stock.")
                choice=str(input("Avez-vous besoin d'autre chose ? (oui/non) : "))
                if choice=="oui":
                    sells=0
                    intro()
                elif choice=="non":
                    fin(nb1,nb2,nb3)
                return
            price_per_stylo = 1.5 
            sells1 = nb1 * price_per_stylo
            choice=str(input("Avez-vous besoin d'autre chose ? (oui/non) : "))
            if choice=="oui":
                sells=0
                intro()
            elif choice=="non":
                fin(nb1,nb2,nb3)
        case 2:
            
            nb2 = int(input("Combien de cahiers souhaitez-vous acheter ? : "))
            if nb2 > stockcahier:
                print("Désolé, nous n'avons pas assez de stock pour cette quantité de cahiers. Nous en avons que", stockcahier,"en stock.")
                choice=str(input("Avez-vous besoin d'autre chose ? (oui/non) : "))
                if choice=="oui":
                    sells=0
                    intro()
                elif choice=="non":
                    fin(nb1,nb2,nb3)
                return
            price_per_cahier = 4.2
            sells2 = nb2 * price_per_cahier
            choice=str(input("Avez-vous besoin d'autre chose ? (oui/non): "))
            if choice=="oui":
                sells=0
                intro()
            elif choice=="non":
                fin(nb1,nb2,nb3)
        case 3:
            
            nb3 = int(input("Combien de cle USB souhaitez-vous acheter ? "))
            if nb3 > stockusb:
                print("Désolé, nous n'avons pas assez de stock pour cette quantité de clés USB. Nous en avons que", stockusb,"en stock.")
                choice=str(input("Avez-vous besoin d'autre chose ? (oui/non) : "))
                if choice=="oui":
                    sells=0
                    intro()
                elif choice=="non":
                    fin(nb1,nb2,nb3)
                return
            price_per_usb = 9.9
            sells3 = nb3 * price_per_usb
            choice=str(input("Avez-vous besoin d'autre chose ? (oui/non) : "))
            if choice=="oui":
                sells=0.0
                intro()
            elif choice=="non":
                fin(nb1,nb2,nb3)
        case 4:
            jour = []
            for i in range(7):
                montant = float(input(f"Jour {i+1} - Entrez le montant des ventes pour ce jour : "))
                if montant < 0:
                    print("Veuillez saisir un montant positif ou zéro.")
                    continue
                jour.append(montant)
            total_semaine = sum(jour)
            moyenne = total_semaine / 7
            jours_sup_moy = sum(1 for d in jour if d > moyenne)
            print("\nStatistiques de vente sur 1 semaine :")
            print("Total semaine :", f"{total_semaine:.2f} €")
            print("Moyenne journalière :", f"{moyenne:.2f} €")
            print("Nombre de jours supérieurs à la moyenne :", jours_sup_moy)
        case _:
            print("Article non disponible.")
            choice=str(input("Avez-vous besoin d'autre chose ? (oui/non) : "))
            if choice=="oui":
                sells=0.0
                intro()
            elif choice=="non":
                fin(nb1,nb2,nb3)
    return



def fin(nb1,nb2,nb3):
    vip = str(input("Êtes-vous un client VIP ? (oui/non) : "))
    global totalttc, totalht, remiseht, remisettc, remise, sells1, sells2, sells3
    remise = 0
    remiseht = remise
    remisettc = remise
    totalht = sells1 + sells2 + sells3
    if totalht > 50:
        totalttc = totalht * 0.9
        remiseht = 1
    totalttc = totalht * 1.2
    if totalttc > 100:
        totalttc = totalttc * 0.8
        remisettc = 2

    print("Le total de vos achats est de :", totalttc, "€.\nVous avez achetez : \n",nb1," stylo(s)",nb2," cahier(s)",nb3," clé(s) USB\nMerci pour votre visite au Magashop!")
    if remiseht == 1 or vip == "oui":
        print("Vous avez bénéficié d'une remise de 10% pour un montant total hors taxe supérieur à 50€.")
    if remisettc == 2:
        print("Vous avez bénéficié d'une remise de 20% pour un montant total toutes taxes comprises supérieur à 100€.")
    if remiseht == 0 and remisettc == 0 and vip == "non":
        print("Vous n'avez bénéficié d'aucune remise.")
    return

def intro():
    global sells
    sells = int(input("Quel article souhaitez-vous acheter ? (1 pour Stylo, 2 pour Cahier, 3 pour Clé USB). Ou voulez vous génerez des statistiques (4) ? : "))
    ventes()
    return

intro()