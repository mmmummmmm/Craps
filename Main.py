import random
from craps_functions import roll_dice, win_message, lose_message
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

#first roll
dice = roll_dice()
dice_sum = dice[0] + dice[1]
if dice_sum == 7 or dice_sum == 11:
    win_message()
elif dice_sum == 2 or dice_sum == 3 or dice_sum == 12:
    lose_message()
else:
    goal = dice_sum
    print(f"\nNow the goal is: {goal}\nIf the sum of your dice is {goal}, You win. If at any point you get 7, you lose!\n")
    while True:
        input ('\nTo roll the dice again, press ENTER . . ')
        dice = roll_dice()
        if dice[0] + dice[1] == goal:
            win_message()
            break
        if dice[0] + dice[1] == 7:
            lose_message()
            break

