# Rock Paper Scissor;
print("Aye Warrior!!! ")
import random

def play():
    while True:
        try:
           opt_user = input("Choose Attack plan. \n"
                      "R for Rock, P for Paper, S for Scissors\n>>> ").upper()
           comp = random.choice(["R", "P", "S"])
           if opt_user == comp:
            print("TIE")
            print()
           elif opt_user_is_win(opt_user, comp):
            print("VICTORY IS YOURS!")
            print()
           elif opt_user_is_loss(comp, opt_user):
              print("You Lost")
              print()
           else: print("Invalid")
           print()
        except EOFError:
           break

def opt_user_is_win(user, AI):
    if user == "R" and AI == "S" or user == "P" and AI == "R" or user == "S" and AI == "P":
        return True
def opt_user_is_loss(AI, user):
   if AI == "R" and user == "S" or AI == "P" and user == "R" or AI == "S" and user == "P":
        return True

play() 