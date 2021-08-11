import prompt
from random import randint

def brain_even():

    answers = ['yes', 'no']

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    counter = 0
    while counter <= 3:

        if counter == 3:
            return f'Congratulations, {name}!'

        random_number = randint(1, 100)
        print(f'Question: {random_number}')

        answer = prompt.string('Your answer: ')

        while True:
            if answer in answers:
                break
            return 'Please answer only with yes or no'

        is_even = random_number % 2 == 0

        if is_even and answer == 'yes':
            print('Correct!')
            counter += 1
            continue
        elif is_even and answer == 'no':
            print(
                f'\'no\' is wrong answer ;(. Correct answer was \'yes\'\nLet\'s try again, {name} !')
            break

        if not is_even and answer == 'no':
            print('Correct!')
            counter += 1
            continue
        elif not is_even and answer == 'yes':
            print(
                f'\'yes\' is wrong answer ;(. Correct answer was \'no\'\nLet\'s try again, {name} !')
            break
