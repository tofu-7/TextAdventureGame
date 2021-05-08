import numpy as np
import random as r

class character:
    def __init__(self):
        self.str = r.randrange(1,50) + r.randrange(1,51) - 1
        self.dex = r.randrange(1,50) + r.randrange(1,51) - 1
        self.int = r.randrange(1,50) + r.randrange(1,51) - 1
        self.hlt = r.randrange(1,50) + r.randrange(1,51) - 1
        self.species = species()
        return

    def CreateCharacter(self, speciesList, specialityList):
        #get input on stats
        #species
        #speciality
        return

#species
class species:
    def __init__(self, sName="", strb=0, dexb=0, intb=0, hltb=0): #TODO work out how to do abilities lol (see bottom of file)
        self.name = sName
        self.strbonus = strb
        self.dexbonus = dexb
        self.intbonus = intb
        self.hltbonus = hltb
        return


#specialty
class speciality:
    def __init__(self, sName=""):
        self.name = sName
        return


#TODO abilities ideas
# have set types of mechanics
# 
#
#
#
#
#
#
#
# ideas are hard
# yeah i got no ideas