# Here are the rules of the game:

# The player should roll two dice. If the sum of both of them is 7 or 11 the player wins.
# If the sum is 2, 3 or 12 (craps) the casino wins. If during the first roll the sum is 4, 5, 6, 8, 9 or 10, 
# that number becomes the “goal” number. 
# To win, the player should roll the dice till they roll the goal number again. 
# If the player rolls a 7 before rolling the goal number, they lose. 



# Your task is to recreate this game using Python. 
# Your program should roll two dice and output the sum of two random numbers. 
# By following the rules of the game, your program should decide whether the player wins or loses. 
import random

def roll_dice():
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    total = num1 + num2
    print(f"You rolled {num1} + {num2} = {total}")
    return total

def game_with_goal(goal_number):
    print(f"Your goal number is {goal_number}. Keep rolling!")
    while True:
        total = roll_dice()
        if total == 7:
            print("You rolled a 7. You lost to the casino!")
            break
        elif total == goal_number:
            print("You rolled your goal number! You win!")
            break

def game():
    print("Rolling dice...")
    total = roll_dice()

    if total in [7, 11]:
        print("You win!")
    elif total in [2, 3, 12]:
        print("The casino wins.")
    elif total in [4, 5, 6, 8, 9, 10]:
        game_with_goal(total)
    else:
        print("Try again!")

game()