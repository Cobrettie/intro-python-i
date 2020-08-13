# Rock, Paper, Scissors

# rock > scissors
# scissors > paper
# paper > rock


### Things to improve ###
# list here

import random

# Returns 0 for a tie
# Returns 1 for user win
# Returns -1 for ai win
def compare_choices(user_choice, ai_choice):
    if user_choice == ai_choice:
        return 0
    # player wins
    elif (user_choice == 'r' and ai_choice == 's') or \
        (user_choice == 'p' and ai_choice == 'r') or \
        (user_choice == 's' and ai_choice == 'p'):
        return 1
    # player loses
    else:
        return -1
    

options = ['r', 'p', 's']

user_wins = 0
ai_wins = 0
ties = 0

# Keep program running until user stops
while True:
    user_choice = input("Choose: r for rock, p for paper, s for scissors, or 'quit' to quit: ")

    if user_choice == 'quit':
        print('Come back soon')
        break
    elif user_choice not in options:
        print('Invalid input')
        continue

    ai_choice = random.choice(options)
    print('AI chooses', ai_choice)

    result = compare_choices(user_choice, ai_choice)

    if result == 0:
        print('Tie!')
        ties += 1
    elif result == 1:
        print('You Won!')
        user_wins += 1
    elif result == -1:
        print('You Lost!')
        ai_wins += 1
    else:
        print('Invalid input, or something went wrong!')
        continue


    print('user wins', user_wins)
    print('ai wins', ai_wins)