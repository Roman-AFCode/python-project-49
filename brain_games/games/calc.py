# Игра калькулятор

import prompt
import random
import operator

# print('What is the result of the expression?')

operator = ['+', '-', '*']
operator_random = random.choice(operator)

num_1 = random.randint (1, 100)
num_2 = random.randint (1, 100)

answer = f'{num_1} {operator_random} {num_2}'

def expression():
    index = 0
    win_score = 3
    congrats = f'Congratulations, {name}'
    while index < win_score:
        operator = ['+', '-', '*']
        operator_random = random.choice(operator)
        num_1 = random.randint (1, 100)
        num_2 = random.randint (1, 100)
        answer = f'{num_1} {operator_random} {num_2}'
        print('Question:', answer)
        index += 1
        user_answer = prompt.string('Your answer: ')
    print(congrats)


expression()




# в игред должен быть вопрос игры и правильный ответ
