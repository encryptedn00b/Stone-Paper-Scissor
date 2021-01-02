from random import randint
import sys
import time
import os
i = 0
import sys
while True:
        sys.stdout.write('\rLoading Game     |')
        time.sleep(0.1)
        sys.stdout.write('\rLoading Game.    /')
        time.sleep(0.1)
        sys.stdout.write('\rLoading Game..   -')
        time.sleep(0.1)
        sys.stdout.write('\rLoading Game...  \\')
        time.sleep(0.1)
        i = i+1
        if i >= 20:
        	os.system('cls')
        	break

t = ["Stone", "Paper", "Scissors"]
computer = t[randint(0,2)]

while True:
    
    print('Stone, Paper, Scissor')
    player = input("Enter Your Choice:-")
    if player == computer:
        print("Tie!")
    elif player == "Stone":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissor":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissor":
        if computer == "Stone":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    computer = t[randint(0,2)]