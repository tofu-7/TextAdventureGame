import random as r
import player as plyr

#TODO Character System

#init species
SpeciesList = []
SpeciesList.append(plyr.species("Human",0,0,0,0))

#init specialties
SpecialitiesList = []
SpecialitiesList.append(plyr.speciality("Generic Person or Something"))

ply = plyr.character()
ply.CreateCharacter(SpeciesList, SpecialitiesList)

print(ply.str)
print(ply.dex)
print(ply.int)
print(ply.hlt)

#TODO Location System

#TODO Game Mechanics
