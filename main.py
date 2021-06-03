import random as r
import player as plyr
import location as loc

#TODO Character System

#init species
SpeciesList = []
SpeciesList.append(plyr.species("Human",0,0,0,0))

#init specialties
SpecialitiesList = []
SpecialitiesList.append(plyr.speciality("Generic Person or Something"))

ply = plyr.character()
ply.CreateCharacter(SpeciesList, SpecialitiesList)

#TODO Location System
locList = [] #TODO move this to a .JSON?
locList.append(loc.location(len(locList), "Everlook", 
    "A small town nestled in the snow, bustling with rowdy folk.", [1]))
locList.append(loc.location(len(locList),"Chad's Cabin", 
    "A wood cabin on the outskirts of Everlook, home to the famous adventurer Chad Kylgem",[0]))


#TODO Game Mechanics

#Game Opening / Test
print("Finish Character Creation Y/N") #TODO placeholder
input("> ")

curLoc = 0 #Variable keeps track of id of current location

while True:
    locList[curLoc].enter()
    pIn = input("> ").lower() #TODO move to other file and formalize all possible actions this is a PLACEHOLDER

    #TODO make system to move to
    