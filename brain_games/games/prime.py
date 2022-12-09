# игра простое ли число?
from random import randint


print('Answer "yes" if given number is prime. Otherwise answer "no".')


def game_function():
    random_number = randint(1, 100)
    question = str(f'Question: {random_number}')
    if random_number > 1:
        for i in range(2, random_number):
            if (random_number % i) == 0:
                result = 'no'
                break
            else:
                result = 'yes'
    else:
        result = 'no'
    return result, question
