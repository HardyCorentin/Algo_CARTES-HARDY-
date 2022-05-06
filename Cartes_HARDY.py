import random

class Cartes :
    def __init__(self, namee, manacoste, descriptione) :
        self.__name=namee
        self.__manacost=manacoste
        self.__description=descriptione
        self.__visible = False
        self.used = False
    def getName(self):
        return self.__name
    def getManacost(self):
        return self.__manacost
    def getDescription(self) :
        return self.__description
#________________________________________________________________________________________________

class Mage :
    def __init__(self, namee, maxmanae,pv):
        self.__name = namee
        self.__maxmana = maxmanae
        self.__manaavailable = 10
        self.__hp = pv
        self.__hand=[random.randint(1,3),random.randint(1,3),random.randint(1,3),random.randint(1,3)]
        self.__discard =0
        self.dead = False
    
    
    def getName(self):
        return self.__name

    def setHand(self) :
        if self.__hand[0] == 1 :
            self.__hand[0] = Blast
        elif self.__hand[0] == 2 :
            self.__hand[0] = Cristal
        elif self.__hand[0] == 3 :
            self.__hand[0] = Creature
        #____
        if self.__hand[1] == 1 :
            self.__hand[1] = Blast
        elif self.__hand[1] == 2 :
            self.__hand[1] = Cristal
        elif self.__hand[1] == 3 :
            self.__hand[1] = Creature
        #____
        if self.__hand[2] == 1 :
            self.__hand[2] = Blast
        elif self.__hand[2] == 2 :
            self.__hand[2] = Cristal
        elif self.__hand[2] == 3 :
            self.__hand[2] = Creature
        #____
        if self.__hand[3] == 1 :
            self.__hand[3] = Blast
        elif self.__hand[3] == 2 :
            self.__hand[3] = Cristal
        elif self.__hand[3] == 3 :
            self.__hand[3] = Creature

        return self.__hand
    
    
    def getMaxmana(self):
        return self.__maxmana
    
    
    def getmanaavailable(self):
        return self.__manaavailable
    
    
    def gethp(self):
        return self.__hp
    
    
    def getdiscard(self):
        self.__discard
    
    
    def checkifdead(self):
        if self.__hp <= 0 :
            print(self.__name,"is dead.")
            return self.dead == True
        else:
            print(self.__name,"survives")


    def manaregen(self):
        self.__manaavailable =self.__maxmana
#______________________________________________________________________________________________
class Cristal(Cartes) :
    def __init__(self):
        self.manaregen = 5
        Cartes.__init__(self,"Mana Cristal",0,"Helps replenish your mana.")
    def getManaregen(self):
        return self.manaregen
#______________________________________________________________________________________________
class Creature(Cartes) :
    def __init__(self,pv, dmg):
        self.hp=pv
        self.damages=dmg
        Cartes.__init__(self,"Creature",4,"Summons a monster on the field to help you out.")
#______________________________________________________________________________________________
class Blast(Cartes) :
    def __init__(self):
        Cartes.__init__(self,"Blast",5,"Use to deal damages to creatures or a Mage")
        self.damages = self.__manacost
    def getDamages(self):
        return self.damages
    def getManacost(self):
        return self.__manacost



joueur1 = Mage ("Player1",10,25)
joueur2 = Mage ("Player2",10,25)


while joueur1.gethp() >0 and joueur2.gethp() >0 :
    print(joueur1.getName,"'s turn to play")
    print("Il vous reste",joueur1.getmanaavailable,"mana.")
    print(joueur1.setHand)
    print("Que choisissez vous ?")
    playerintput = int(input("(Donnez le numéro de la carte)"))
