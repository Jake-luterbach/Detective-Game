##############################################################################
#Module: Detective Game - Win conditions
##############################################################################
# Imports --------------------------------------------------------------------
# Functions ------------------------------------------------------------------
def win_condition():
    print("After 15 minutes, everyone meet at the Town Square and wait for you")
    print("Rebecca: Do you find who is the one stands behind \
these disappearacne events, Alex")
    print("Alex: Yes, I do.")
    culprit = input("It is ")
    if culprit == "Mayor Evelyn Brooks":
        print("You have find the right culprit. Thank you for playing")
    else:
        print("Sorry, but the culprit is still outside the law. You should play again\
and organize your thinking this time, detective")