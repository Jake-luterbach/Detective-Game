##############################################################################
#Title: Detective Game
#Class: CS 30        
#Date: May 28, 2024            
#Coders Name: HuuThienLe, John Jiang, Jake Luterbach           
#Version: 001                                      
##############################################################################
'''
A detective game where the player tries to discover the mystery of a missing 
persons case.
'''
#-----------------------------------------------------------------------------
# Imports --------------------------------------------------------------------
import player as p
import Map
#-----Functions---------------------------------------------------------------
def moveMenu():
    p.playerObject.movement()
    print("You are in " + Map.Ravenswood_Map[p.playerObject.locY][p.playerObject.locX])


Map.readMap("townMap.txt")
Map.readMap("undergroundMap.txt")

moveMenu()
#----Main---------------------------------------------------------------------