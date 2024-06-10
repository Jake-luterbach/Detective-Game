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
import NPCs


options = ["Move", "Change Floors", "View Map", "Write Map"]
#-----Functions---------------------------------------------------------------
def moveMenu():
    moveChoice=input("Choose the direction you want to go: ").capitalize()
    p.playerObject.movement(moveChoice)
    print("You are in " + Map.Ravenswood_Map[p.playerObject.locY][p.playerObject.locX])


def moveFloors():
    p.playerObject.changeFloor()
    print("You are now underground.")


def playerChoice():
    for x in options:
        print(f"*{x}")
    choice = input("Choose what you want to do: ").capitalize()
    return choice
    

def npc():
    if Map.Ravenswood_Map[p.playerObject.locY][p.playerObject.locX] == NPCs.mayor.loc:
        print("There is an NPC!")
        print("\n")
        NPCs.mayor.NPC_Dialogue()
        NPCs.mayor.NPC_Clues()


def menu():
    print("Here are your options.")
    option = playerChoice()
    npc()
    if option == "Move":
        moveMenu()
    #elif option == "Change Floors":
        #moveFloors()
    elif option == "View Map":
        Map.readMap("townMap.txt")

#writeMap(Underground_Tunnels_Map, "undergroundMap.txt")
#Map.readMap("undergroundMap.txt")

def main():
    # Player starts with town map
    Map.writeMap(Map.Ravenswood_Map, "townMap.txt", )
    menu()


#----Main---------------------------------------------------------------------
main()
