
import random


def roll_dice():
    dice= []
    for i in range(2):
        dice.append (random.randint(1,6))
    
    print(f"Your first dice is {dice[0]} | Your second dice is {dice[1]} | Total = {dice[0] + dice[1]}")
    return dice


def win_message():
    print("\n   ~\~ ~|~ ~/~  YOU WON!")

def lose_message():
    print ("\n     You know the rules! CASINO WON! :(")
