import random

def roll_dice():
    roll_dice = input("Roll dice? (Yes/No): ")
    
    while roll_dice.lower() == "Yes".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("Dice rolled {} and {}".format(dice1, dice2))

        roll = input("Roll dice again? (Yes/No): ")

roll_dice()