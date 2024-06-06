##############################################################################
#Module: Detective Game - Map
##############################################################################
# Imports --------------------------------------------------------------------
from tabulate import tabulate
# Functions ------------------------------------------------------------------
Ravenswood_Rooms = {
    "Dr.Graham’s Office" : {"Description" : "An office of a reclusive psychologist"},
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
    "Ravenswood Town Square" : {"Description" : "Place that all of events're happened"},
    "Old Asylum" : {"Description" : "The derelict asylum where many past and\
        recent victims were last seen"},
    "Emily’s Family House" : {"Description" : "Family of victim from \
        the disapperances 15 years ago"}
    }


Ravenswood_Map = [["Dr.Graham’s Office", "Police Station", "Mayor Brooks’Office",
           "Mercer’s Cottage", "Blackwood Manor"],
          ["The Lighthouse", "Cemetery", "RavenswoodTown Square", 
          "Old Asylum", "Emily's Family House"]] 


Underground_Tunnels_Rooms = {
    "Storage room" : {"Description" : "A room where most of useless items are thrown"},
    "Long Tunnel" : {"Description": "A dark and long tunnel, \
        acording to the map there should be 2 entrances"}, 
    "Secret Room Entrance" : {"Description" : "Concealed behind a bookcase in the \
        secret room of Blackwood Manor"}, 
    "Entrance from Cemetery" : {"Description" : "Concealed within a mausoleum in \
        the cemetery."}, 
    "Hidden Chamber" : {"Description" : "Seems like a not yet finished chamber"},
    "Entrance from Old Asylum" : {"Description" : "A hidden door in the basement of \
        the old asylum, cover by debris and old medical equipment"},
    "Blackwood Manor Secret Room" : {"Description" : "Where Henry stores historical\
        artifacts and documents and does his research without interruption"}}


Underground_Tunnels_Map = [["Storage room", "Long Tunnel", "Long Tunnel",
                            "Secret Room Entrance"], 
                           ["Entrance from Cemetery", "Hidden Chamber", 
                            "Entrance from Old Asylum", "Blackwood Manor Secret Room"]] 


def writeMap(map, mapFile):
    try:
        with open(mapFile, 'w') as file:
            file.write(tabulate(map, tablefmt = "grid"))
    except:
        print("An error occurred when writing the file.")
    else:
        print("This is a map.")
    finally:
        print("Good luck, detective.")


def readMap(mapFile):
    try:
        with open(mapFile, 'r') as file:
            print(file.read())
    except:
        print("An error occurred when reading the file.")
    else:
        print("This is a map.")
    finally:
        print("Good luck, detective.")


writeMap(Ravenswood_Map, "townMap.txt", )
writeMap(Underground_Tunnels_Map, "undergroundMap.txt")
