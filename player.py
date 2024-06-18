##############################################################################
#Module: Detective Game - Player
##############################################################################
# Imports --------------------------------------------------------------------
import Map as m
# Functions ------------------------------------------------------------------
class Player:
    def __init__(self, locY, locX, locZ):
        self.locY = locY
        self.locX = locX
        self.locZ = locZ

    
    def movement(self, choice):
        """
        Moves the player around the town map if within boundaries
        """
        self.choice = choice
        if self.choice == "W" and self.locY > 0:
            #moves player up on the town map
            self.locY -= 1
        elif self.choice == "S" and self.locY < 1:
            #moves player down on the town map
            self.locY += 1
        elif self.choice == "A" and self.locX > 0:
            #moves player left on the town map
            self.locX -= 1
        elif self.choice == "D" and self.locX < 4:
            #moves player right on the town map
            self.locX += 1
        else:
            #if player tries to move off the map it prints this message
            print("You can't go there detective,you have a job to do!")
        return True


    def undergroundMovement(self, choice):
        """
        Moves the player around the underground map if 
        within boundaries
        """
        self.choice = choice
        if self.choice == "W" and self.locY > 0:
            #moves player up on underground map
            self.locY -= 1
        elif self.choice == "S" and self.locY < 1:
            #moves player down on underground
            self.locY += 1
        elif self.choice == "A" and self.locX > 0:
            #moves player left on underground map
            self.locX -= 1
        elif self.choice == "D" and self.locX < 3:
            #moves player right on underground map
            self.locX += 1
        else:
            #if player tries to move off the map it prints this message
            print("You can't go there detective,you have a job to do!")
        return True
        

    def changeFloor(self):
        """Changes floors for the player"""
        # Forcefully switch the player's coordinates from above ground
        # to below ground or vice versa, based on each room. 
        if [self.locY,self.locX,self.locZ] == [1,4,0]:
            [self.locY,self.locX,self.locZ] = [1,3,1]
        elif [self.locY,self.locX,self.locZ] == [1,3,1]:
            [self.locY,self.locX,self.locZ] = [1,4,0]
        elif [self.locY,self.locX,self.locZ] == [1,1,0]:
            [self.locY,self.locX,self.locZ] = [1,0,1]
        elif [self.locY,self.locX,self.locZ] == [1,0,1]:
            [self.locY,self.locX,self.locZ] = [1,1,0]
        elif [self.locY,self.locX,self.locZ] == [1,3,0]:
            [self.locY,self.locX,self.locZ] = [1,2,1]
        elif [self.locY,self.locX,self.locZ] == [1,2,1]:
            [self.locY,self.locX,self.locZ] = [1,3,0]


playerObject = Player(1, 2, 0)