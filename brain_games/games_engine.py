# движок запускающий и проверяющий игры
import prompt


def start_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_RULE)
    counter = 0
    while counter != 3:
        result, question = game.get_game_result()
        print(question)
        answer = prompt.string('Your answer: ')
        if answer != result:
            return print(f"'{answer}' is wrong answer ;(., "
                         f"Correct answer was '{result}'.\
                           \nLet's try again, {name}!")
        elif answer == result:
            print('Correct!')
            counter += 1
    print(f'Congratulations, {name}!')
