# Игра на определение чётности
from random import randint


def game_function():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    random_number = randint(1, 99)
    if random_number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    question = str(f'Question: {random_number}')
    return result, question