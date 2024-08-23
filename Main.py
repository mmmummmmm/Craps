import random

input('''
      Welcome to Craps.
      In Craps you get to have a once in a life time oppurtinity to win billions of fake dollar.

      Here are the rules:
      The player should roll two dice. 
      If the sum of both of them is 7 or 11 the player wins. 
      If the sum is 2, 3 or 12 (craps) the casino wins. 
      
      If during the first roll the sum is 4, 5, 6, 8, 9 or 10, that number becomes the “goal” number. 
      To win, the player should roll the dice till they roll the goal number again. 
      If the player rolls a 7 before rolling the goal number, they lose.

               
                  To begin press Enter . . .
      ''')

def roll_dice():
    dice= []
    for i in range(2):
        dice.append (random.randrange(1,6))
    
    print(f"Your first dice is {dice[0]} | Your second dice is {dice[1]} | Total = {dice[0] + dice[1]}")
    return dice


def win_message():
    print("     YOU WON!")

def lose_message():
    print ("     You know the rules! CASINO WON!")

dice= roll_dice()
dice_sum = dice[0]+dice[1]
if dice_sum == 7 or dice_sum == 11:
    win_message()
elif dice_sum == 2 or dice_sum == 3 or dice_sum == 12:
    lose_message()
else:
    goal= dice_sum
    print(f"Now the goal is: {goal}\n")
    while True:
        dice=roll_dice()
        if dice[0]+dice[1]==goal:
            win_message()
            print ('win')
            break
        if dice[0]+dice[1]==7:
            lose_message()
            break

