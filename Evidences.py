##############################################################################
#Module: Detective Game - Evidences
##############################################################################
# Imports --------------------------------------------------------------------
# Functions ------------------------------------------------------------------
Items = {"Missing Person Reports": {"Description": "A stack of Missing Persons Reports"+
                                    ", with details of the victims. One stands out to "+
                                    "you: John Mercer.", 
                                    "Location": [0,1], 
                                    "Actions": ["Take","Leave"], "Requirements":"none"},
        "Mercer's Journal Diary": {"Description": "Cryptic journal entries by John "+
                                   "Mercer detailing his investigation into a similar "+
                                   "disappearance 15 years ago.",
                                  "Location": [0,3],
                                  "Actions": [],
                                  "Requirements": ""},
        "Patient Records": {"Description": "Files on patients who were part of "+
                            "experimental treatments, many of whom are among "+
                            "the missing.",
                             "Location": [1,3],
                             "Actions": [],
                             "Requirements": ""},
        "Photo": {"Description": "An old photograph showing John Mercer and "+
                  "Dr.Lucas Graham together, suggesting a past connection.",
                   "Location": [0,0],
                   "Actions": [],
                   "Requirements": ""},
        "Historical Manuscript": {"Description": "An ancient manuscript detailing "+
                                  "the town’s history, including references to a curse"+
                                  " and maybe the formation of a secret group.",
                                   "Location": [],
                                   "Actions": [],
                                   "Requirements": ""},
        "Underground Tunnel Map": {"Description": "A detailed map of the hidden "+
                                   "tunnels beneath the town, with marked locations of"+
                                   " interest.",
                                    "Location": [],
                                    "Actions": [],
                                    "Requirements": ""},
        "Ritual Artifacts": {"Description": "Strange artifacts, including ritualistic "+
                             "items and symbols linked to the secret group.",
                              "Location": [],
                              "Actions": [],
                              "Requirements": ""},
        "Mercer's Final Notes": {"Description": "Final notes by John Mercer detailing "+
                                 "his discovery of the secret group and their plans. "+
                                 "Ends abruptly, hinting at his capture or demise.",
                                  "Location": [4,1],
                                  "Actions": ["take","leave"],
                                  "Requirements": ""},
        "Confession Letter": {"Description": "A letter written by Mayor Evelyn Brooks",
                               "Location": [0,2],
                               "Actions": ["take","leave"],
                               "Requirements": "None"},
        "Old Article": {"Description": "An article about the similar of disappearances \
              15 years ago with one of the victims is Emily",
                         "Location": [0,3],
                         "Actions": ["take","leave"],
                         "Requirements": "None"},
        "Lighthouse Ledger": {"Description": "A ledger containing records of \
              the secret group’s meetings and rituals,\
               with detailed accounts of their actions and plans.",
                               "Location": [1,0],
                               "Actions": ["take","leave"],
                               "Requirements": "None"}}

Evidences = []
class Evidence:
    def __init__(self, Identify, take):
        self.Identify = Identify
        self.take = take
    def find_evidence(self):
        found_evidence = False
        print("you are inspecting the area")
        
        
        
        