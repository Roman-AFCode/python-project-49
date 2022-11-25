#!/usr/bin/env python3

import random
from brain_games.cli import welcome_user


name = welcome_user()

def parity_check():
    even_answer = 'yes'
    odd_answer = 'no'
    counter = 0

    print('Answer "yes" if the number is even, otherwise answer "no".')
    while counter != 3:
        num = random.randint(1, 99)
        print('Question:', num)
        player_answer = input('Your answer: ')
        if num % 2 == 0 and player_answer.lower() == 'yes':
            print('Correct!')
            counter += 1
        elif num % 2 == 1 and player_answer.lower() == 'no':
            print('Correct!')
            counter += 1
        elif num % 2 == 1 and player_answer.lower() == 'yes':
            print(f"'{player_answer}' is wrong answer ;(. Correct answer was '{odd_answer}'. \nLet's try again, {name}!")
            break
        elif num % 2 == 0 and player_answer.lower() == 'no':
            print(f"'{player_answer}' is wrong answer ;(. Correct answer was '{even_answer}'. \nLet's try again, {name}!")
            break
        else:
            print('The answer n, u or dskjfkl is not correct! \nAnswer "yes" if the number is even, otherwise answer "no".')
            break
    if counter == 3:
        print(f'Congratulations, {name}!')
