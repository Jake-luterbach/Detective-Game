##############################################################################
#Module: Detective Game - Player
##############################################################################
# Imports --------------------------------------------------------------------
# Functions ------------------------------------------------------------------
class Player:
    def __init__(self, locationX, locationY, locationZ):
        self.locationX = locationX
        self.locationY = locationY
        self.locationZ = locationZ

    
    def movement(self, choice):
        self.choice = choice
        if choice == "W":
            self.locationY -= 1
        elif choice == "S":
            self.locationY += 1
        elif choice == "A":
            self.locationX -= 1
        elif choice == "D":
            self.locationX += 1


    def changeFloor(self):
        if self.locationZ == 0:
            self.locationZ += 1
        elif self.locationZ == 1:
            self.locationZ -= 1


playerObject = Player(0, 0, 0)

playerObject.movement()