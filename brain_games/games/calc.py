# Игра калькулятор
from random import randint, choice


print('What is the result of the expression?')


def game_function():
    result = 0
    num_1 = randint(1, 99)
    num_2 = randint(1, 99)
    random_operator = choice('+-*')
    question = str(f'Question: {num_1} {random_operator} {num_2}')
    if random_operator == '+':
        result = num_1 + num_2
    elif random_operator == '-':
        result = num_1 - num_2
    elif random_operator == '*':
        result = num_1 * num_2
    return str(result), question
