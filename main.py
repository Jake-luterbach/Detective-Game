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


options = ["Move", "Map", "Talk", "Inspect", "Inventory", "Quit"]

requirement = False
#-----Functions---------------------------------------------------------------
print("Detective Game")

print()
# Starting story and informations about the game.
print("In the small, seeming idyllic town of Ravenswood, a community has been shaken by\
 a series of mysterious disappearances. The local police are baffled and unable to find\
 any leads or connections between the victims. A detective Alex Harper, a seasoned\
 investigator with a troubled past, who is called to discover the truth behind these\
 events. When you arrive at the Ravenswood Town, you begin in the Town Square. You see\
 a person at the Town Square.")

print()

print("???: Hi Detective, I'm Clarke, a newspaper interview. \
I'm here to help you. Why don't we going to the police officer first for some \
informations about the victims. Here is the map of this area.")


def moveFloors():
    """
    This function gives the player the option to change floors if they
    are in certain rooms.
    """
    print()
    print("You realize that there is a secret entrance where you can \
change floors.")
    # Give user choice to change floors
    upOrDown = input("Do you want to try changing floors?\
    (Yes or No) ").capitalize()
    if upOrDown == "Yes":
        p.playerObject.changeFloor()
        print("You have now changed floors.")
        print()
        # Check if player is above ground or underground
        # Print the according room name and description so player knows
        if p.playerObject.locZ == 0:
            print("You are in " + \
Map.Ravenswood_Map[p.playerObject.locY][p.playerObject.locX])
            print(Map.Ravenswood_Rooms[Map.Ravenswood_Map\
[p.playerObject.locY][p.playerObject.locX]]["Description"])
        elif p.playerObject.locZ == 1:
            print("You are in " +\
Map.Underground_Tunnels_Map[p.playerObject.locY][p.playerObject.locX])
            print(Map.Underground_Tunnels_Rooms\
[Map.Underground_Tunnels_Map[p.playerObject.locY]\
[p.playerObject.locX]]["Description"])

    elif upOrDown == "No":
        print("You decide to not do anything for now.")
    else:
        print("Invalid Input")
        moveFloors()


def change_floors_re(a, b, c):
    '''Requirements need to change floors.'''
    global requirement
    # Check coordinates of player locations to see if they are in 
    # a room that you can change floors
    if [p.playerObject.locY, p.playerObject.locX, \
        p.playerObject.locZ] == [a, b, c]:
        requirement = True
        if requirement:
            # Give player option to move floors if in a room where they can
            moveFloors()
        requirement = False


def moveMenu():
    """Menu for calling moving functions and print player location"""
    moveChoice=input("Choose the direction you want to go (w,a,s,d):\
").capitalize()
    print()
    # Check if player is above ground or below ground
    # Print the corresponding room and room description after moving
    if p.playerObject.locZ == 0:
        p.playerObject.movement(moveChoice)
        print("You are in " + \
              Map.Ravenswood_Map[p.playerObject.locY]\
              [p.playerObject.locX])
        print(Map.Ravenswood_Rooms[Map.Ravenswood_Map\
            [p.playerObject.locY][p.playerObject.locX]]["Description"])
    elif p.playerObject.locZ == 1:
        p.playerObject.undergroundMovement(moveChoice)
        print("You are in " +\
              Map.Underground_Tunnels_Map[p.playerObject.locY]\
              [p.playerObject.locX])
        print(Map.Underground_Tunnels_Rooms\
            [Map.Underground_Tunnels_Map[p.playerObject.locY]\
            [p.playerObject.locX]]["Description"])


def playerChoice():
    '''
    Gives the player a choice for what they want to do,
    used in other functions
    '''
    for x in options:
        # Print all player's options
        print(f"*{x}")
    choice = input("Choose what you want to do: ").capitalize()
    print("\n")
    return choice
    

def npc(npc):
    '''
    When used it activates the NPCs dialogue and clues through 
    the NPCs module
    '''
    print("There is a person here!")
    # Call the NPC dialogue and clues based on which NPC player interacts with
    npc.NPC_Dialogue()
    npc.NPC_Clues()
    print("\n")


def npcAvailable():
    """Checks if there is an NPC available at the player's location"""
    for name in NPCs.npcNames:
        # Return the NPC if there is one that exists at the player's location
        # Otherwise, return false
        if [p.playerObject.locY, p.playerObject.locX, \
            p.playerObject.locZ] == name.loc:
            return name
    else:
        return False
            

def inventory():
    """Prints the player's inventory of items"""
    print("Inventory Menu")
    # Check if player's inventory is empty or not
    if e.Evidences == []:
        print("There is nothing in your inventory yet.")
    else:
        # If not, print player's inventory
        for item in e.Evidences:
            print("*" + item + ": " + e.Items[item]["Clues"])

    
def menu():
    """
    Main menu where player chooses actions. Calls action functions.
    """
    print()
    print("Here are your options.")
    # User input for player to choose out of all the options
    option = playerChoice()
    if option == "Move":
        moveMenu()
    elif option == "Map":
        Map.writeMap(Map.Ravenswood_Map, "townMap.txt")
        Map.readMap("townMap.txt")
        # Only print the map for above ground if player has not retrieved
        # underground map yet
        for item in e.Evidences:
            if item == "Underground Tunnel Map":
                Map.writeMap(Map.Underground_Tunnels_Map, 
                             "undergroundMap.txt")
                Map.readMap("undergroundMap.txt")
    elif option == "Talk":
        # Check if an NPC exists
        if npcAvailable() is not False:
            npc(npcAvailable())
        else:
            print("There is nobody here!")
    elif option == "Inspect":
        e.find_evidence()
    elif option == "Inventory":
        inventory()
    elif option == "Quit":
        # Set end game condition to true
        NPCs.end = True
        

#----Main---------------------------------------------------------------------
while True and not NPCs.end:
    change_floors_re(1, 3, 0)
    change_floors_re(1, 4, 0)
    change_floors_re(1, 1, 0)
    change_floors_re(1, 0, 1)
    change_floors_re(1, 2, 1)
    change_floors_re(0, 3, 1)
    menu()
