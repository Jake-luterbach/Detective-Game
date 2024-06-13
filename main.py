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
import Evidences as e


options = ["Move", "Map", "Talk", "Inspect", "Inventory"]
#-----Functions---------------------------------------------------------------
print("In the small, seeming idyllic town of Ravenswood, a community has been shaken by\
 a series of mysterious disappearances. The local police are baffled and unable to find\
 any leads or connections between the victims. A detective Alex Harper, a seasoned\
 investigator with a troubled past, who is called to discover the truth behind these\
 events. When you arrive at the Ravenswood Town, you begin in the Town Square. You see\
 a person at the Town Square.")


def moveFloors():
    print("You realize that there is a secret entrance where you can change floors.")
    upOrDown = input("Do you want to try changing floors? (Yes or No)").capitalize()
    if upOrDown == "Yes":
        p.playerObject.changeFloor()
        print("You have now changed floors.")
    else:
        print("You decide to not do anything for now.")


def moveMenu():
    moveChoice=input("Choose the direction you want to go (w,a,s,d): ").capitalize()
    p.playerObject.movement(moveChoice)
    print()
    if p.playerObject.locZ == 0:
        print("You are in " + \
              Map.Ravenswood_Map[p.playerObject.locY][p.playerObject.locX])
        print(Map.Ravenswood_Rooms[Map.Ravenswood_Map[p.playerObject.locY][p.playerObject.locX]]["Description"])
    elif p.playerObject.locZ == 1:
        print("You are in " +\
              Map.Underground_Tunnels_Map[p.playerObject.locY][p.playerObject.locX])
        print(Map.Underground_Tunnels_Rooms[Map.Underground_Tunnels_Map[p.playerObject.locY][p.playerObject.locX]]["Description"])
   # if Map.Ravenswood_Map[p.playerObject.locY][p.playerObject.locX] == \
    #"Blackwood Manor":
      #  moveFloors()


def playerChoice():
    for x in options:
        print(f"*{x}")
    choice = input("Choose what you want to do: ").capitalize()
    print("\n")
    return choice
    

def npc(npc):
    print("There is a person here!")
    npc.NPC_Dialogue()
    npc.NPC_Clues()
    print("\n")


def npcAvailable():
    for name in NPCs.npcNames:
        if [p.playerObject.locY, p.playerObject.locX, p.playerObject.locZ] == name.loc:
            return name
    else:
        return False
            

def inventory():
    print("Inventory Menu")
    if e.Evidences == []:
        print("There is nothing in your inventory yet.")
    else:
        for item in e.Evidences:
            print("*" + item + ": " + e.Items[item]["Clues"])

    
def menu():
    print()
    print("Here are your options.")
    option = playerChoice()
    if option == "Move":
        moveMenu()
    #elif option == "Change Floors":
        #moveFloors()
    elif option == "Map":
        Map.writeMap(Map.Ravenswood_Map, "townMap.txt")
        Map.readMap("townMap.txt")
        for item in e.Evidences:
            if item == "Underground Tunnel Map":
                Map.writeMap(Map.Underground_Tunnels_Map, "undergroundMap.txt")
                Map.readMap("undergroundMap.txt")
    elif option == "Talk":
        if npcAvailable() is not False:
            npc(npcAvailable())
        else:
            print("There is nobody here!")
    elif option == "Inspect":
        e.find_evidence()
    elif option == "Inventory":
        inventory()
        

#----Main---------------------------------------------------------------------
while True and not NPCs.end:
    menu()
