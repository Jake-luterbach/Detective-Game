
class NPC:
    def __init__(self,Name,clues):
        self.Name = Name
        self.clues = clues
    def NPC_Dialogue(self):
        if self.Name == "Mayor Evelyn Brooks":
            print("Hey there I'm evelyn brooks the mayor of Ravenswood!")
        if self.Name == "Dr. Lucas Graham":
            print("Hi, Detective I'm Dr. Graham, the psychologist")
        if self.Name == "Samantha Clarke":
            print("Hey Detective" + 
                  ", Do you have infromation about the case for the press?")
        if self.Name == "Henry Blackwood":
            print("Hello Detective, if you have any questions please do ask")
        if self.Name == "Rebbeca Mercer":
            print("Hey Alex! Have you spoken to my father yet?")
            
    def NPC_Clues(self):
        active = True
        clues = active
        if clues == active:
            print("Test")