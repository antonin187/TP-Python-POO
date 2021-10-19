from ClassDate import *
from ClassID import *

def Inscrition() :

    carnet = []

    while True :
        print("\nSaisissez la date d'aujourd'hui")
        while True:
            try:
                day = int(input("   Jour : "))
                month = int(input("   Mois : "))
                year = int(input("   Année : "))

                laDate = ClassDate(day, month, year)
                break
            except ValueError:
                print("Vous devez saisir des nombres entiers")
            except notAValideYear:
                print("L'année doit être comprise entre 1000 et 9999.")
            except notAValideMonth:
                print("Cette date n'existe pas")
            except notAValideDay:
                print("Cette date n'existe pas")

        print("La date d'aujourd'hui est le :", laDate)
        saisie = input("Confirmez-vous cette date ? (Répondre O pour oui ou N pour non) : ").upper()

        if day == 1 and month == 1 and year == 9999  and saisie == "O" :
            print("\nFin des inscriptions.\n")
            break

        while saisie != "O" and saisie != "N"  :
            saisie = input("Réponse incorrecte. Répondre O pour oui ou N pour non : ").upper()

        if saisie == "O" :
            pass
        else :
            print("")
            continue

        while True :

            sortir = False

            saisie = input("\nSouhaitez-vous ajouter une nouvelle inscription aujourd’hui ? (Répondre O pour oui ou N pour non) : ").upper()

            while saisie != "O" and saisie != "N"  :
                saisie = input("Réponse incorrecte. Répondre O pour oui ou N pour non : ").upper()

            if saisie == "O" :
                while True:

                    again = False

                    try:
                        nom = input("Nom : ")
                        while nom == "" :
                            nom = input("")

                        prenom = input("Prénom : ")
                        while prenom == "" :
                            prenom = input("")

                        for element in carnet :
                            if nom == element.nom and prenom == element.prenom :
                                print("Cette identité apparait déjà dans la liste des inscrits.")
                                saisie = input("Voulez-vous poursuivre l'inscription ? (Répondre O pour oui ou N pour non) : ").upper()
                                while saisie != "O" and saisie != "N" :
                                    saisie = input("Réponse incorrecte. Répondre O pour oui ou N pour non : ").upper()
                                
                                if saisie == "N" :
                                    again = True

                        if again == True :
                            print("\nReprenons :")
                            continue

                        while True :
                            print("Date d'inscription :")
                            day = int(input("   Jour : "))
                            month = int(input("   Mois : "))
                            year = int(input("   Année : "))

                            newInscription = ClassID(prenom, nom, day, month, year)

                            if laDate > newInscription :
                                print("La date est passée")

                                saisie = input("Voulez-vous saisir une autre date d'inscription ? (Répondre O pour oui ou N pour non) : ").upper()
                                while saisie != "O" and saisie != "N" :
                                    saisie = input("Réponse incorrecte. Répondre O pour oui ou N pour non : ").upper()

                                if saisie == "O" :
                                    continue
                                else :
                                    sortir = True
                            break

                        break

                    except ValueError:
                        print("Vous devez saisir des nombres entiers")
                    except notAValideYear:
                        print("L'année doit être comprise entre 1000 et 9999.")
                    except notAValideMonth:
                        print("Cette date n'existe pas")
                    except notAValideDay:
                        print("Cette date n'existe pas")

                if sortir == True :
                    continue

                print("Récapitulatif :", newInscription)

                saisie = input("Confirmez-vous cette inscription ? (Répondre O pour oui ou N pour non) : ").upper()

                while saisie != "O" and saisie != "N" :
                    saisie = input("Réponse incorrecte. Répondre O pour oui ou N pour non : ").upper()

                if saisie == "O" :
                    print("Inscription validée.")
                    carnet.append(newInscription)
                else :
                    print("Inscription annulée.")

            else :
                print("\nFin des inscriptions pour aujourd'hui.")
                break

    affichageTableau(carnet)

def affichageTableau(laListe) :
    i = 0
    print("Liste des inscriptions (rangée numéro d'inscription) :")
    print("{:15} {:15} {:15} {:15}".format("Numéro :", "Nom :", "Prénom :", "Date d'inscription :"))
    for element in laListe :
        i += 1
        print("{:15} {:15} {:15} {}/{}/{}".format(str(i), element.nom, element.prenom, element.day, element.month, element.year))

    i = 0

    listNames = []

    for element in laListe :
        listNames.append(element.nom)

    sorted_list = sorted(listNames)

    print("\nListe des inscriptions (rangée par ordre alphabétique) :")
    print("{:15} {:15} {:15} {:15}".format("Numéro :", "Nom :", "Prénom :", "Date d'inscription :")) 
    for element in laListe :
        i += 1
        print("{:15} {:15} {:15} {}/{}/{}".format(str(i), sorted_list[i-1], element.prenom, element.day, element.month, element.year))

    dateList = []
    k = 0

    for element in laListe :
        dateList.append(ClassDate(element.day, element.month, element.year))

    while True :

        k = 0
        count = 0
        
        while k < len(dateList) :
            try :
                if dateList[k] > dateList[k + 1] :
                    dateList.append(dateList[k])
                    dateList.remove(dateList[k])
                else :
                    count += 1
            except :
                pass 
            k += 1
        if count >= len(dateList) - 1 :
            break

    i = 0

    print("\nListe des inscriptions (rangée par date d'inscription) :")
    print("{:15} {:15} {:15} {:15}".format("Numéro :", "Nom :", "Prénom :", "Date d'inscription :"))
    for element in laListe :
        i += 1
        print("{:15} {:15} {:15} {}/{}/{}".format(str(i), element.nom, element.prenom, dateList[i-1].day, dateList[i-1].month, dateList[i-1].year))

Inscrition()
