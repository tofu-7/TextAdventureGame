class location:
    def __init__(self, lID, lName, lEntDesc, lLinks):
        self.ID = lID
        self.name = lName
        self.enterDesc = lEntDesc
        self.linkLoc = lLinks
        return

    def enter(self):
        print(self.name)
        print(self.enterDesc)
        return
        