import prompt
from random import randint
from brain_games.control import greetings, is_correct_answer

def brain_even():

    answers = {True: 'yes', False: 'no'}

    name = greetings()

    print('Answer "yes" if the number is even, otherwise answer "no".')

    counter = 0
    while counter <= 3:

        if counter == 3:
            print(f'Congratulations, {name}!')
            break

        random_number = randint(1, 100)
        print(f'Question: {random_number}')

        user_answer = prompt.string('Your answer: ')

        is_even = random_number % 2 == 0

        expected_answer = answers.get(is_even)

        if not is_correct_answer(user_answer, expected_answer, name):
            break

        counter += 1
