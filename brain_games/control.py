import prompt


def greetings():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def is_correct_answer(user_answer, expected_answer, name):
    if user_answer == expected_answer:
        print('Correct!')
        return True
    else:
        print(
            f'\'{user_answer}\' is wrong answer ;(. Correct answer was \'{expected_answer}\'') # noqa: E501
        print(f'Let\'s try again, {name}!')
        return False


def gcd(a, b):
    while(b):
        a, b = b, a % b

    return a


def isPrime(n):
    if n > 1:
        for i in range(2, n // 2):
            if (n % i) == 0:
                return('no')
        else:
            return('yes')
    else:
        return('no')
