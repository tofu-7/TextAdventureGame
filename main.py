import random as r
import character as chrt

#TODO Character System

#init species
SpeciesList = []
SpeciesList.append(chrt.species("Human",10,10,10,10))

#init specialties
SpecialitiesList = []
SpecialitiesList.append(chrt.speciality("Generic Person or Something"))

char = chrt.character()
char.CreateCharacter(SpeciesList, SpecialitiesList)

print(char.str)
print(char.dex)
print(char.int)
print(char.hlt)

#TODO Location System

#TODO Game Mechanics
