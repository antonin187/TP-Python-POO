from error import *
class ClassDate(object):

    def __init__(self,day,month,year) :
        self.year = year
        self.month = month
        self.day = day



    @property
    def year(self):
        return self.__year
    
    @property
    def month(self):
        return self.__month
    
    @property
    def day(self):
        return self.__day
    
    
    @year.setter
    def year(self,value):
        #On verifie que la value est bien un entier
        #On verifie que notre value est bien comprise entre 1000 et 9999
        if value<1000 or value>9999:
            raise notAValideYear()
        self.__year = value     
    
    @month.setter
    def month(self,value):
        #On verifie que la value est bien un entier
        
        #On verifie que notre value est bien comprise entre 1 et 12
        if value<1 or value >12:
            raise notAValideMonth()
        self.__month = value    
    

    @day.setter
    def day(self,value):
        #On verifie que la value est bien un entier

        #On verifie que la value est  bien comprise entre 1 et le nombre de jours maximum dans le mois rentré par l'utilisateur # en fonction de si c'est une annee bisextile ou non aussi
        if value > self.dayInAMonth(self.year)[self.month-1] or value<1:
            raise notAValideDay()
        self.__day= value
    
    def __str__(self):
        #On s'assure de bien afficher les valeurs inferieurs a 10 avec un 0 avant
        if self.day<10:
            theDay=  "0" + str(self.day)
        else:
            theDay= str(self.day)
        if self.month<10:
            theMonth="0" + str(self.month)
        else:
            theMonth= str(self.month)
        return   theDay + "/" + theMonth + "/" + str(self.year)


    #Pour savoir si une annee est bisextile ou non
    def leapyear(self,year) :
        if (year%4==0 and year%100!=0 or year%400==0):
            return True
        else:
            return False
    #retourne le tableau des jours dans chaque mois en fonction de si on est dans une annee bisextile ou non 
    def dayInAMonth(self,year):
        
        if self.leapyear(year) :
            return [31,29,31,30,31,30,31,31,30,31,30,31]
        else: 
           return [31,28,31,30,31,30,31,31,30,31,30,31]

    #surcharche operateur ">" pour bien verifier quune date est anterieur a une autre 
    def __gt__(self,other):
        if self.year> other.year:
            return True
        elif self.year==other.year:
            if self.month>other.month:
                return True
            elif self.month==other.month:
                if self.day>other.day:
                    return True
                else:
                    return False
            else:
                return False
        else: 
            return False

    # Methode pour comparer deux date par rapports a leur mois et jour 
    def compareMonthAndDay(self,other):
        if self.month > other.month:
            return True
        elif self.month== other.month:
            if self.day>other.day:
                return True
            if self.day==other.day:
                return "even"
            else: 
                return False
        else:
            return False
            

  #surcharge d'operateur "-"
    def __sub__(self,other):
        #On verifie bien que la date est anterieure avant de commencer 
        if self > other:
            #On compare le mois et le jour des dates sans regarder l'annee
            #Si le mois et le jours sont identique on soustrait juste 
            if self.compareMonthAndDay(other)=="even":
                theYears= self.year-other.year
                theDays=0
            elif self.compareMonthAndDay(other) :
                #dans ce cas l'année est egal a une simple soustraction de nos deux annees
                theYears= self.year-other.year
                theDays=0
                # si les deux dates ont le meme mois on additione a days la soustraction des deux jours  
                if self.month == other.month :
                    theDays += (self.day-other.day)
                else:
                    # si le mois est superieure les jours correspondent a l'additions des mois complets entre les deux dates
                    for i in range( other.month,self.month -1):
                        theDays += self.dayInAMonth(self.year)[i]
                    #puis au rajout des jours restants dans chacun des mois 
                    theDays += (self.dayInAMonth(self.year)[other.month-1]- other.day)
                    theDays += self.day
            else:
                #si la date sans lanne est inferieure a lautre date 
                #on calcule le nombre d'année
                theYears= self.year - other.year-1
                theDays=0
                #le nombre de jours correspond aux nombre de jour entre l'autre date(un an avant )  et la fin de l'annee
                for i in range (other.month,12):
                    theDays += self.dayInAMonth(self.year-1)[i]
                #additioné aux nombre de jours entre le debut de l'année et notre date 
                for i in range (0,self.month-1):
                    theDays += self.dayInAMonth(self.year)[i]
                #puis on rajoute les jours restant dans l'autre date pour finir le mois 
                theDays += (self.dayInAMonth(self.year-1)[other.month-1] - other.day)
                #et enfin on rajoute les jours entamé dans la date 
                theDays += self.day
        
            
                
        else:
            #erreur si la date n'est pas anterieure 
            raise substractError()

        return "votre âge est de " + str(theYears) + " ans et " + str(theDays)+" jours (à un jour près)."