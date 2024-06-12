##############################################################################
#Module: Detective Game - Player
##############################################################################
# Imports --------------------------------------------------------------------
# Functions ------------------------------------------------------------------
class Player:
    def __init__(self, locY, locX, locZ):
        self.locY = locY
        self.locX = locX
        self.locZ = locZ

    
    def movement(self, choice):
        self.choice = choice
        if self.choice == "W" and self.locY > 0:
            self.locY -= 1
        elif self.choice == "S" and self.locY < 1:
            self.locY += 1
        elif self.choice == "A" and self.locX > 0:
            self.locX -= 1
        elif self.choice == "D" and self.locX < 4:
            self.locX += 1
        else:
            print("You can't go there detective, you have a job to do!")
        return True
            

    def changeFloor(self):
        if self.locZ == 0:
            self.locZ += 1
        elif self.locZ == 1:
            self.locZ -= 1


playerObject = Player(1, 2, 0)