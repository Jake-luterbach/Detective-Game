##############################################################################
#Module: Detective Game - Actions
##############################################################################
# Imports --------------------------------------------------------------------
import player as p
import Evidences as e
# Functions ------------------------------------------------------------------
inventory = []


def Actions(act):
    print("You done inspect the room, and find the item")
    act = int(input("Your action is "))
    if act == 1:
        inventory.append[e.item]