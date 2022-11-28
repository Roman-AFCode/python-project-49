#!/usr/bin/env python3

#Вывод должен получиться следующий:
#
# brain-even
#
# Welcome to the Brain Games!
# May I have your name? Sam
# Hello, Sam!
# Answer "yes" if the number is even, otherwise answer "no".
# Question: 15
# Your answer: no
# Correct!
# Question: 6
# Your answer: yes
# Correct!
# Question: 7
# Your answer: no
# Correct!
# Congratulations, Sam!

from brain_games.scripts.even import welcome_user, parity_check


def main():
    welcome_user()
    parity_check()


if __name__ == '__main__':
    main()
