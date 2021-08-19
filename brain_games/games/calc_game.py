import random
import operator
from brain_games.control import greetings, is_correct_answer


def brain_calc():
    name = greetings()

    print('What is the result of the expression?')

    counter = 0
    while counter <= 3:

        if counter == 3:
            print(f'Congratulations, {name}!')
            break

        operators = {'+': operator.add, '-': operator.sub, '*': operator.mul}

        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        op = random.choice(list(operators.keys()))

        expected_answer = int(operators.get(op)(num1, num2))

        user_answer = int(input(
            f'Question: {num1} {op} {num2}\nYour answer: '))

        if not is_correct_answer(user_answer, expected_answer, name):
            break

        counter += 1
