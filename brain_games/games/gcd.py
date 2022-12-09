# игра наибольший общий делитель
from random import randint


print('Find the greatest common divisor of given numbers.')


def game_function():
    result = 0
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    question = str(f'Question: {num_1} {num_2}')
    while num_2 > 0:
        num_1, num_2 = num_2, num_1 % num_2
        result = num_1
    return str(result), question
