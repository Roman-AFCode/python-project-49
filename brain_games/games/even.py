# Игра на определение чётности
from random import randint


GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def get_game_result():
    random_num = randint(1, 99)
    question = str(f'Question: {random_num}')
    if is_even(random_num) is True:
        result = 'yes'
    if is_even(random_num) is False:
        result = 'no'
    return result, question
