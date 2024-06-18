##############################################################################
#Module: Detective Game - NPCs
##############################################################################
# Imports --------------------------------------------------------------------
import Map
import Evidences as e
import win

# Set end game condition/win condition to initially false
end = False

# Functions ------------------------------------------------------------------
class NPC:
    def __init__(self, name, clues, q1, q2, a1, a2, loc, evi):
        '''
        Information on the NPCs, including name, clues, 
        questions and location
        '''
        self.name = name
        self.clues = clues
        self.q1 = q1
        self.q2 = q2
        self.a1 = a1
        self.a2 = a2
        self.loc = loc
        self.evi = evi
    
    
    def NPC_Dialogue(self):
        """
        The dialogue of every NPC, printed when player 
        interacts with them
        """
        if self.name == "Mayor Evelyn Brooks":
            # Dialogue for Mayor Evelyn 
            print("Mayor Evelyn Brooks: The mayor of Ravenswood")
            print("Hey there,I'm Evelyn Brooks,the mayor of Ravenswood\
! Thank you for coming to help us with these disappearances.")
        if self.name == "Dr. Lucas Graham":
            # Dialogue for Dr.Lucas Graham
            print("Dr.Lucas Graham: A psychologist who worked on the \
disappearances with John Mercer")
            print("Hi detective, I'm Dr. Graham the psychologist")
        if self.name == "Emily's Family Home":
            # Dialogue for Emily's family 
            print("Emily's family: 15 years ago emily was one of \
the victims in a mass disappearance, there are no suspects yet.")
            print("Who are you and what do you want from us?")
        if self.name == "Henry Blackwood":
            # Dialogue for Henry Blackwood
            print("Henry Blackwood: An eccentric historian with \
a deep knowledge of the town’s dark past")
            print("Hello Detective, if you have any \
questions please do ask.")
        if self.name == "Rebbeca Mercer":
            # Dialogue for Rebbeca Mercer
            print("Rebecca Mercer: Daughter of Alex’s mentor,\
seeking closure for her father’s disappearance")
            print("Hey Alex! Have you found my father yet?")

    
    def NPC_Clues(self):
        '''Clues the NPCs give based on questions'''
        global end
        active = True
        print("You decide to question " + self.name + ".")
        self.clues = active
        if self.clues == active:
            #Ask's questions based on each character
            print("Excuse me, " + self.name + 
                  ", can I ask a few questions?")
            print()
            print("(1) " + self.q1)
            for item in e.Evidences:
                if self.evi == item:
                    print("(2) " + self.q2)
            try:
                #answers to the Questions that lead to clues
                print()
                Question = int(input("You choose (1 or 2):"))
                if Question == 1:
                    print("(1) " + self.a1)
                if Question == 2:
                    print("(2) " + self.a2)
                    if self.name == "Mayor Evelyn Brooks":
                        win.win_condition()
            except:
                print("There was an error. Please try again.")
    

mayor = NPC("Mayor Evelyn Brooks", True, "Ask about where Mercer is?",
            "Can you ask everyone to meet at the town hall? \
I think I know who stands behind these disappearances.",
            "I'm not sure where Mr. Mercer is, have you tried \
looking at his cottage?",
            "Oh... sure. We'll meet you there in a few minutes.",
            [0,2,0],
            "Confession Letter")

doctor = NPC("Dr. Lucas Graham", True, "Ask about the events?",
            "Ask about the photo of him and John Mercer together",
            "Oh, I would say that there were some similiar events\
like these from a long time ago. It's like a curse",
            "Well, him and I investigated the disappearances \
15 years ago. If you already checked his cottage, you may see\
the article about 15 years ago. Mercer and I didn't find anything \
about it even with the help of Emily. It was my shame to lead\
to what happened to Emily.", [0,0,0], "Photo")

henry = NPC("Henry Blackwood", True,
    "Do you know anything about John Mercer and his disappearance?", 
    "Ask about Mercer's journal?", "Oh, you ask about that annoying \
guy. I don't know, maybe he was trying to find some clues about the\
disappearances 15 years ago. He would come back after a few months.\
It's always like that",
    "I would say that was his shame. He used Emily like a tool to find\
the truth. But do you know what? He lost her and found NOTHING. \
And now you say the same events happened again.", [1,4,0], 
    "Mercer's Journal Diary")

rebecca = NPC("Rebbeca Mercer", True, "Ask about her father?",
    "Ask about her father's journal?",
    "Actually, he often disappeared for a few months. \
    But he always left me a note detailing when he will come back.",
    "No, I don't know anything about them, maybe Henry knows.", 
    [0,3,0],
    "Mercer's Journal Diary")

emily = NPC("Emily's Family Home", True, "Ask about Emily?",
    "Do you know where she disappeared to?",
    "She's always been a kind and good girl. She was gonna have a \
bright future if she didn't help that guy try and find \
something that didn't exist.",
    "We don't know. But I found her bracelet at Old Asylum. \
If you want to find anything more, you should go there.\
But there isn't anything left over there. My husband \
already went many times", [0,4,0], "Old Article")


npcNames = [mayor, doctor, henry, rebecca, emily]


def Clarke(item):
    '''prints clues when used'''
    print(e.Items[item]["Clues"])