##############################################################################
#Module: Detective Game - Map
##############################################################################
# Imports --------------------------------------------------------------------
from tabulate import tabulate
# Functions ------------------------------------------------------------------
Ravenswood_Rooms = {
    "Dr. Graham’s Office" : {"Description" : ""},
    "Police Station" : {"Description": "The Ravenswood police station"}, 
    "Mayor Brooks’ Office" : {"Description" : "The office of Mayor Brooks"}, 
    "Mercer’s Cottage" : {"Description" : "The old Mercer's cottage, " + 
        "made from wood and is very eerie"}, 
    "Blackwood Manor" : {"Description" : "Henry’s home,\
        which contains ancient tomes and artifacts"},
    "The Lighthouse" : {"Description" : "The final confrontation site,\
        located on the outskirts of Ravenswood"},
    "Cemetery" : {"Description" : "The town's cemetery, often associated with\
        mysterious activities at night"}, 
    "RavenswoodTown Square" : {"Description" : ""},
    "Old Asylum" : {"Description" : "The derelict asylum where many past and\
        recent victims were last seen"},
    "Emily’s Family House" : {"Description" : "Family of victim from \
        the disapperances 15 years ago"}
    }


Ravenswood_Map = [["Dr. Graham’s Office", "Police Station", "Mayor Brooks’Office",
           "Mercer’s Cottage", "Blackwood Manor"],
          ["The Lighthouse", "Cemetery", "RavenswoodTown Square", 
          "Old Asylum", "Emily's Family House"]] 


Underground_Tunnels_Rooms = {
    "Ritual Artifacts" : {"Description" : ""},
    "Long Tunnel" : {"Description": ""}, 
    "Secret Room Entrance" : {"Description" : ""}, 
    "Entrance from Cemetery" : {"Description" : ""}, 
    "Hidden Chamber" : {"Description" : ""},
    "Entrance from Old Asylum" : {"Description" : ""},
    "Blackwood Manor Secret Room" : {"Description" : ""}}


Underground_Tunnels_Map = [["Ritual Artifacts", "Long Tunnel", "Long Tunnel",
                            "Secret Room Entrance"], 
                           ["Entrance from Cemetery", "Hidden Chamber", 
                            "Entrance from Old Asylum", "Blackwood Manor Secret Room"]] 


def writeMap():
    try:
        with open("mapFile.txt", 'w') as file:
            file.write(tabulate(Ravenswood_Map, tablefmt = "grid"))
    except:
        print("An error occurred when writing the file.")
    else:
        print("This is a map of Ravenswood Town.")
    finally:
        print("Good luck, detective.")


def readMap():
    try:
        with open("mapFile.txt", 'r') as file:
            print(file.read())
    except:
        print("An error occurred when reading the file.")
    else:
        print("This is a map of Ravenswood Town.")
    finally:
        print("Good luck, detective.")

writeMap()
readMap()