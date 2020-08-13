# Rock, Paper, Scissors

# rock > scissors
# scissors > paper
# paper > rock

import random

options = ['r', 'p', 's']

user_wins = 0
ai_wins = 0

# Keep program running until user stops
while True:
    user_choice = input("Choose: r for rock, p for paper, s for scissors ")
    ai_choice = random.choice(options)
    print('AI chose', ai_choice)


    user_victory = 'User has won!'
    ai_victory = 'AI has won!'

    if (user_choice == 'r' and ai_choice == 's'):
        user_wins += 1
        print(user_victory)
    elif (user_choice == 'p' and ai_choice == 'r'):
        user_wins += 1
        print(user_victory)
    elif (user_choice == 's' and ai_choice == 'p'):
        user_wins += 1
        print(user_victory)

    elif (ai_choice == 'r' and user_choice == 's'):
        ai_wins += 1
        print(ai_victory)
    elif (ai_choice == 'p' and user_choice == 'r'):
        ai_wins += 1
        print(ai_victory)
    elif (ai_choice == 's' and user_choice == 'p'):
        ai_wins += 1
        print(ai_victory)
    else:
        print('Either a tie, or incorrect input')
        continue


    print('user wins', user_wins)
    print('ai wins', ai_wins)