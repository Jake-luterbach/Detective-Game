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
            print("Hey Alex! Have you found my father yet?")

    
    def NPC_Clues(self):
        active = True
        Question = input("Question " + self.name + " (1 or 2)")
        clues = active
        if clues == active:
            if self.name == "Mayor Evelyn Brooks":
                print("1) Ask about where Mercer is?")
                print("2) ask about the confession letter")
                if Question == 1:
                    print("I'm not sure where Mr.Mercer is"+
                          "have you tried looking at his cottage?")
                if Question == 2:
                    print("oh uhh, it's nothing")
            elif self.name == "Dr.Lucas Graham":
                print("1) ask about what happened to mercer")
                print("2) ask about ")
                if Question == 1:
                    print("2")
                if Question == 2:
                    print("1")