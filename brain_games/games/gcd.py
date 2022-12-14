# игра наибольший общий делитель
from random import randint
from math import gcd


GAME_RULES = 'Find the greatest common divisor of given numbers.'


def get_game_result():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    question = str(f'Question: {num_1} {num_2}')
    result = gcd(num_1, num_2)
    return str(result), question
