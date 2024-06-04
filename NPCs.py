##############################################################################
#Module: Detective Game - NPCs
##############################################################################
# Imports --------------------------------------------------------------------
# Functions ------------------------------------------------------------------
class NPC:
    def __init__(self, name, clues):
        self.name = name
        self.clues = clues

    
    def NPC_Dialogue(self):
        if self.name == "Mayor Evelyn Brooks":
            print("Hey there I'm evelyn brooks the mayor of Ravenswood!")
        if self.name == "Dr. Lucas Graham":
            print("Hi detective, I'm Dr. Graham the psychologist")
        if self.name == "Samantha Clarke":
            print("Hey Detective" + 
                  ", Do you have infromation about the case for the press?")
        if self.name == "Henry Blackwood":
            print("Hello Detective, if you have any questions please do ask")
        if self.name == "Rebbeca Mercer":
            print("Hey Alex! Have you spoken to my father yet?")

    
    def NPC_Clues(self):
        active = True
        clues = active
        if clues == active:
            print("Test")