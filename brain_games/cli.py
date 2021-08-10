import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    greetings = f'Hello, {name}!'
    print(greetings)
