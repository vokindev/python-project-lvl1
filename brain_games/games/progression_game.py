import random
from brain_games.control import greetings, is_correct_answer


def brain_progression():

    name = greetings()
    print('What number is missing in the progression?')

    counter = 0
    while counter <= 3:

        if counter == 3:
            print(f'Congratulations, {name}!')
            break

        start = random.randint(1, 100)
        length = random.randint(5, 10)
        step = random.randint(1, 100)

        arr = []

        x = start

        for i in range(length):
            arr.append(x)
            x += step

        expected_answer = random.choice(arr)
        arr[arr.index(expected_answer)] = '..'
        arr_str = ' '.join(map(str, arr))

        user_answer = int(input(f'Question: {arr_str}\nYour answer: '))

        if not is_correct_answer(user_answer, expected_answer, name):
            break

        counter += 1
