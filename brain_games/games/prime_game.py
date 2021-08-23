import random
from brain_games.control import greetings, is_correct_answer, isPrime


def brain_prime():

    name = greetings()

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    counter = 0
    while counter <= 3:

        if counter == 3:
            print(f'Congratulations, {name}!')
            break

        n = random.randint(1, 100)

        expected_answer = isPrime(n)

        user_answer = input(f'Question: {n}\nYour answer: ')

        if not is_correct_answer(user_answer, expected_answer, name):
            break

        counter += 1
