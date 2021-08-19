import random
from brain_games.control import greetings, gcd, is_correct_answer


def brain_gcd():
    name = greetings()

    print('Find the greatest common divisor of given numbers.')

    counter = 0
    while counter <= 3:

        if counter == 3:
            print(f'Congratulations, {name}!')
            break

        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

        expected_answer = gcd(num1, num2)

        user_answer = int(input(
            f'Question: {num1} {num2}\nYour answer: '))

        if not is_correct_answer(user_answer, expected_answer, name):
            break

        counter += 1
