import random
from random import choice

users_score = 0
computers_score = 0
#users chooses either rock paper or scissors
#computer randomly chooses either one of the three
#outcome
game_limit = input("please enter your preferred game limit: ")
game_limit = int(game_limit)

while users_score < game_limit and computers_score < game_limit:
    print("...rock...")
    print("...paper...")
    print("...scissors...")
    users_choice = input("(Enter you choice): ") # users chooses rock paper or scissors
    if users_choice != "rock" and users_choice != "paper" and users_choice != "scissors": # validates the choice 
        print("please enter a valid choice")

    computers_choice = random.choice(["rock", "paper", "scissors"]) # computer randomly chooses rock paper or scissors
    print(f"the computer chooses {computers_choice}")

    if users_choice == computers_choice:
        print("it is a tie")
    
    elif users_choice == "rock":
        if computers_choice == "paper":
            computers_score += 1
            print("the computer wins")
        else:
            users_score += 1
            print("the user wins")
            
    elif users_choice == "paper":
        if computers_choice == "scissors":
            computers_score += 1
            print("the computer wins")
        else:
            users_score += 1
            print("the user wins")

    elif users_choice == "scissors":
        if computers_choice == "rock":
            computers_score += 1
            print("the computer wins")
        else:
            users_score += 1
            print("the user wins")
    
    print(f"user score: {users_score} computer score: {computers_score}")
    
if users_score == game_limit:
    print("the user wins the entire game")
    pipo = input("do you want to play again? (y/n)")
    if pipo == "y":
        print("yes you want that wouldnt you")
    else:
        print("ok bye")
elif computers_score == game_limit:
    print("the computer wins the entire game")
    pipo = input("do you want to play again? (y/n)")
    if pipo == "y":
        print("yes you want that wouldnt you")
    else:
        print("ok bye")
    
print("the game is over")
