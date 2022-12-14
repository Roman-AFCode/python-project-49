# Игра калькулятор
from random import randint, choice


GAME_RULES = 'What is the result of the expression?'
OPERATORS = choice('+-*')


def calculator(num_1, num_2):
    if OPERATORS == '+':
        return num_1 + num_2
    elif OPERATORS == '-':
        return num_1 - num_2
    elif OPERATORS == '*':
        return num_1 * num_2


def get_game_result():
    num_1 = randint(1, 99)
    num_2 = randint(1, 99)
    question = str(f'Question: {num_1} {OPERATORS} {num_2}')
    result = calculator(num_1, num_2)
    return str(result), question
