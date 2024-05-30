class NPC:
    def NPCs(self,Name,clues):
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
NPC_talk = NPCS