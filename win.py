##############################################################################
#Module: Detective Game - Win conditions
##############################################################################
# Imports --------------------------------------------------------------------
import Evidences as e
import NPCs
import Map
import player as p
# Functions ------------------------------------------------------------------
def clues_prove():
    global answer
    print("Please choose one of the evidences in your inventory to prove your thinking")
    for item in e.Evidences:
        print(item + e.Items[item]["CLues"])
    answer = input("Alex: ")


def win_condition():
    print("After 15 minutes, everyone meets at the Town Square and waits for you")
    print("Rebecca: Did you find out who's behind \
the disappearances, Alex?")
    answer = input("Alex: ")
    if answer == "yes":   
        culprit = input("It is ")
        if culprit == "Mayor Evelyn Brooks":
            print("Dr.Graham: Huh? What lead you to that decision, detective?")
            clues_prove()
            if answer == "Lighthouse Ledger":
                print("Henry: Oh, you mean the records of our meeting. It just a small\
party where we have a discussion about wine.")
                print("Alex: How about if I say all of you are involved in this case. \
You guys are all the members of the secret group called 'The Keepers of Shadow'.")
                clues_prove()
                if answer == "Mercer's Final Notes":
                    print("Alex: This note has show that both of you guys are the \
member of that. According to Mercer, the members of that group worship the unknown god,\
and believe it can give them power to control the world.To satisfy their god, each \
15 years they will sacrifice people to gain the God’s attention.")
                    print("Mayor: So how it is related to me. I didn't know they are\
the members of that group.")
                    print("Alex: No. Mayor, you know it. This is the evidence show that you cooperated with them.")
                    clues_prove()
                    if answer == "Confession Letter":
                        print("Alex: Have nothing to say.")
                        print("Thank for playing the game. That's all for now")
                        NPCs.end = True
        else:
            print("Sorry, but the culprit is still on the loose. You should play again \
and organize your thinking this time, detective")
            NPCs.end = True
    elif answer == "no":
        p.playerObject.locX = 2
        p.playerObject.locY = 1
        print(Map.Ravenswood_Rooms[Map.Ravenswood_Map[p.playerObject.locY][p.playerObject.locX]]["Description"])