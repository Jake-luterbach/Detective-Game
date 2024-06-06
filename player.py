##############################################################################
#Module: Detective Game - Player
##############################################################################
# Imports --------------------------------------------------------------------
# Functions ------------------------------------------------------------------
class Player:
    def __init__(self, locX, locY, locZ, choice):
        self.locX = locX
        self.locY = locY
        self.locZ = locZ
        self.choice = choice

    
    def movement(self):
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


playerObject = Player(1, 2, 0, choice=input("Choose the direction you want to go: ").capitalize()))