# движок запускающий и проверяющий игры
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def result_check(game):
    welcome_user()
    counter = 0
    while counter != 3:
        result, question = game.game_function()
        print(question)
        answer = prompt.string('Your answer: ')
        if answer != result:
            print(f"'{answer}' is wrong answer ;(. \
                Correct answer was '{result}'.\
                    \nLet's try again, {name}!")
            break
        elif answer == result:
            print('Correct!')
        counter += 1
    if counter == 3:
        print(f'Congratulations, {name}!')
