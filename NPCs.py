##############################################################################
#Module: Detective Game - NPCs
##############################################################################
# Imports --------------------------------------------------------------------
import Map
import Evidences as e
# Functions ------------------------------------------------------------------
class NPC:
    def __init__(self, name, clues, q1, q2, a1, a2, loc, evi):
        self.name = name
        self.clues = clues
        self.q1 = q1
        self.q2 = q2
        self.a1 = a1
        self.a2 = a2
        self.loc = loc
        self.evi = evi
    
    
    def NPC_Dialogue(self):
        if self.name == "Mayor Evelyn Brooks":
            print("Hey there I'm Evelyn Brooks the mayor of Ravenswood!\
                Thank you for coming to help us with these disappearances events")
        if self.name == "Dr. Lucas Graham":
            print("Hi detective, I'm Dr. Graham the psychologist")
        if self.name == "Emily's Family Home":
            print("Who are you and what do you want from us?")
        if self.name == "Henry Blackwood":
            print("Hello Detective, if you have any questions please do ask")
        if self.name == "Rebbeca Mercer":
            print("Hey Alex! Have you found my father yet?")

    
    def NPC_Clues(self):
        active = True
        Question = int(input("Question " + self.name + " (1 or 2)"))
        self.clues = active
        if self.clues == active:
            Question = int(input("Excuse me." + self.name + \
                                 " Can I ask a few questions?"))
            print("(1) " + self.q1)
            for item in e.Evidences:
                if self.evi == item:
                    print("2" + self.q2)
            if Question == 1:
                print("(1) " + self.a1)
            if Question == 2:
                print("(2) " + self.a2)
        

mayor = NPC("Mayor Evelyn Brooks", True, "Ask about where Mercer is?",
            "Can you ask everyone to meet at the town hall? \
                I think I know who stands behind these disapperances.",
            "I'm not sure where Mr. Mercer is, have you tried looking at his cottage?",
            "Oh... sure. We'll meet you there in a few minutes.", [1,2,0],
            None)
doctor = NPC("Dr. Lucas Graham", True, "Ask about the events?",
            "Ask about the photo of him and John Mercer together?",
            "Oh, I would say that there were some similiar events like these from a \
                long time ago. It likes a curse",
            "Well, him and I used to discovered about the disapperances 15 years ago. \
                If you already checked his cottage, you may see the article about\
                15 years ago. I and John didn't find anything about it even with the \
                help of Emily. It was my shame to lead it happens to Emily.", [0,0,0],
            "Photo")
henry = NPC("Henry Blackwood", True, "Do you know anything about John Mercer and \
                his disappearance?",
            "Ask about John's journal?",
            "Oh, you ask about that annoying guy. I don't know, maybe he going to find\
                some clues about the disapperances 15 years ago. He will come back \
                after a few months. It always like that",
            "I would say that was his shame. He used Emily like a people to find \
                the truth. But do you know what? He lost her and found NOTHING. \
                And now you say the events happend again.", [0,4,0],
            "Mercer's Journal Diary")
rebecca = NPC("Rebbeca Mercer", True, "Ask about her father?",
              "Ask about her father's journal?",
              "Actually, he often disappeared for a few months. But he always let me a\
                note when he will come back.", 
              "No, I don't know anything about them, maybe Henry knows.", [0,3,0],
            "Mercer's Journal Diary")
emily = NPC("Emily's Family Home", True, "Ask about Emily",
           "Do you know where she disappear?",
           "She's always a kind and good girl. She is gonna have a better future if \
            she didn't help that guy find a truth that didn't exist.",
           "We don't know. But I found her bracelet at Old Asylum. If you want to find \
                anything more, you should go there.But there is not anything \
                overthere. My husband go to it many times", [1,4,0],
           "Old Article")