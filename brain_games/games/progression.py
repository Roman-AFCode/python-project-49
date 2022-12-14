# игра арифметическая прогрессия
from random import randint


GAME_RULES = 'What number is missing in the progression?'


def get_game_result():
    random_len = randint(5, 10)
    random_step = randint(1, 5)
    lst = [str(i) for i in range(1, 100, random_step)][:random_len]

    def result_return():
        random_integer = randint(0, len(lst) - 1)
        result = (lst[random_integer])
        lst[random_integer] = '..'
        question = ('Question: ' + (' '.join(lst)))
        return result, question
    return result_return()
