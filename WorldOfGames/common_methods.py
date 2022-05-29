import random
from Live import validate


def generate_number(upper_limit):
    random_number = random.randint(1, upper_limit)
    return random_number


def get_guess_from_user(upper_limit):
    guess_message = f'Please guess the number from 1 to {upper_limit}:'
    is_guess_valid = False
    guess_number = 1
    while not is_guess_valid:
        guess_number = input(guess_message)
        validate_message = f'guess is not valid Please guess the number from 1 to {upper_limit}'
        is_guess_valid = validate(guess_number, 1, upper_limit, validate_message)
    return guess_number

