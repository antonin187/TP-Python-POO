from ClassDate import *

def getYourAGe():
    theDates =[] 
    for i in range(2):
        if i==0:
            print("Saisissez votre date de naissance : ")
        else:
            print("Saisissez la date à laquelle vous souhaitez connaître votre âge : ")
        while True:
            day =input("Jour : ")
            month = input("Mois : ")
            year = input("Année : ")
            try:
                theDates.append(ClassDate(int(day),int(month),int(year)))
                if i==1:
                    theAge = theDates[1]-theDates[0]
                break
            except ValueError:
                print("Vous devez saisir des nombres entiers")
            except notAValideYear:
                print("L'année doit être comprise entre 1000 et 9999.")
            except notAValideMonth:
                print("Cette date n'existe pas")
            except notAValideDay:
                print("Cette date n'existe pas")
            except substractError:
                print("Cette date est antérieure à votre date de naissance.")
        if i==0:
            print("Votre date de naissance est le", theDates[0])
        if i==1:
            print("le", theDates[1], ",", theAge)

getYourAGe()