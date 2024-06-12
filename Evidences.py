##############################################################################
#Module: Detective Game - Evidences
##############################################################################
# Imports --------------------------------------------------------------------
import player as p
import NPCs
# Functions ------------------------------------------------------------------
Evidences = []

Items = {"Missing Person Reports": {"Description": "A stack of Missing Persons Reports,\
            with details of the victims. One stands out to you: John Mercer.",
                "Location": [0,1,0],
                "Clues" : "So our next location is John Mercer's home"},
    "Mercer's Journal Diary": {"Description": "Cryptic journal entries by John \
Mercer detailing his investigation into a similar disappearance 15 years ago.",
                "Location": [0,3,0],
                "Clues" : "According to Mercer's diary, the disappearance events \
used to happen many times with the period of 15 years. Now,the only \
victims' family that we can contact is Emily's parents."},
    "Patient Records": {"Description": "Files on patients who were part of \
experimental treatments, many of whom are among the missing.",
                "Location": [1,3,0],
                "Clues" : "Most of the patient is missing since the treatments, \
seems like this is quite similiar to the missing events from the past and now"},
    "Photo": {"Description": "An old photograph showing John Mercer and \
Dr.Lucas Graham together, suggesting a past connection.",
                "Location": [0,0,0],
                "Clues" : "So John Mercer and Dr.Graham have known each other from \
a long time ago. Maybe, Dr.Graham will know something about the past events "},
    "Historical Manuscript": {"Description": "An ancient manuscript detailing \
the town’s history, including references to a curse and maybe \
the formation of a secret group.",
                "Location": [1,3,1],
                "Clues" : "According to this, there may be a secret society or \
organization in the past. A long time ago, the citizens often killed \
some people to escape the curse."},
    "Underground Tunnel Map": {"Description": "A detailed map of the hidden tunnels \
beneath the town, with marked locations of interest.",
                "Location": [1,3,1],
                "Clues" : "There is also the underground tunnels in this town. \
Does it relate to the disappearances that we explore?"},
    "Ritual Artifacts": {"Description": "Strange artifacts, including ritualistic \
items and symbols linked to the secret group.",
                "Location": [1,1,1],
                "Clues" : "These might be the symbols of the secret society. \
So there is actually a secret society that lasts from the past to now."},
    "Mercer's Final Notes": {"Description": "Final notes by John Mercer detailing \
his discovery of the secret group and their plans. Ends abruptly, hinting at his \
capture or demise.",
                "Location": [1,1,1],
                "Clues" : "Mercer details his discovery of the secret society known as \
the Keepers of the Shadow. He names several key members, including Henry Blackwood and \
Dr. Lucas Graham. Mercer connects recent and past disappearances in Ravenswood to the \
Keepers’ rituals. Mercer warns about an imminent ritual that the Keepers are planning. \
They worship the unknown god, they believe it can give them power to control the world. \
To satisfy their god, each 15 years they will sacrifice people to gain the God’s \
attention."},
    "Confession Letter": {"Description": "A letter written by Mayor Evelyn Brooks",
                "Location": [0,2,0],
                "Clues" : "She has involvement with the secret group, \
and her misguided attempts to protect the town. The smoking gun that reveals the \
mastermind behind the disappearances."},
    "Old Article": {"Description": "An article about the similar of disappearances \
15 years ago with one of the victims is Emily",
                "Location": [0,3,0],
                "Clues" : "Now we have to go to Emily's home. We should use a map \
to find it"},
    "Lighthouse Ledger": {"Description": "A ledger containing records of \
the secret group’s meetings and rituals, with detailed accounts of their actions and \
plans.", "Location": [1,0,0], 
                "Clues" : "Dr.Graham, Henry, and ... even Mayor Brooks!!!"}
}


def find_evidence():
    #self.found_evidence = False
    print()
    print("You are inspecting the area...")
    for item in Items:
        if [p.playerObject.locY, p.playerObject.locX, p.playerObject.locZ] == \
        Items[item]["Location"]:
            print("Oh? There is an item:")
            print(Items[item]["Description"])
            actions = input("Do you want to take the item? (Yes or No): ")
            try:
                if actions.capitalize() == "Yes":
                    #print("You found something")
                    Evidences.append(item)
                    print()
                    print("You successfully stored the item.")
                    print()
                    print("Clarke: ")
                    NPCs.Clarke(item)
                    print()
                if actions.capitalize() == "No":
                    print("You left the item.")
            except:
                print("Invalid input.")
    else:
        print("There is nothing here")