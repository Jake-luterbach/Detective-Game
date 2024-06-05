##############################################################################
#Module: Detective Game - Player
##############################################################################
# Imports --------------------------------------------------------------------
# Functions ------------------------------------------------------------------
class Player:
    def __init__(self, locX, locY, locZ):
        self.locX = locX
        self.locY = locY
        self.locZ = locZ

    
    def movement(self, choice):
        self.choice = choice
        if choice == "W":
            self.locY -= 1
        elif choice == "S":
            self.locY += 1
        elif choice == "A":
            self.locX -= 1
        elif choice == "D":
            self.locX += 1


    def changeFloor(self):
        if self.locZ == 0:
            self.locZ += 1
        elif self.locZ == 1:
            self.locZ -= 1


playerObject = Player(0, 0, 0)


playerObject.movement(choice=input("Direction you want to go is: "))