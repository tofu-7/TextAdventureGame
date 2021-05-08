import random as r

#TODO Character System
#Character Class   
#Specialization Class
#Species Class

#Location System
class Location: #Location Class
    def __init__(self, id, LinkedLocations, EntryText):
        self.LinkedLocations=LinkedLocations
        self.id=id
        self.EntryText=EntryText
        return
    
    def enter(self): 
        print(self.EntryText)
        return

#TODO Game Mechanics

#Main Loop
