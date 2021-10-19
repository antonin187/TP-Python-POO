from ClassDate import *

class ClassID(ClassDate) :

    def __init__(self, prenom, nom, Jour, month, year) :
        ClassDate.__init__(self, Jour, month, year)
        self.prenom = prenom
        self.nom = nom

    @property
    def prenom(self) :
        return self.__prenom

    @property
    def nom(self) :
        return self.__nom

    @prenom.setter
    def prenom(self, value) :
        self.__prenom = value

    @nom.setter
    def nom(self, value) :
        self.__nom = value

    def __str__(self) :
        return str(self.nom) + " " + str(self.prenom) + " " + str(self.day) + "/" + str(self.month) + "/" + str(self.year)