from Live import get_game_level, validate
import common_methods


def compare_result(guess, expected):
    return guess == expected


def play(difficulty):
    secret_number = common_methods.generate_number(int(difficulty))
    guess_from_user = common_methods.get_guess_from_user(difficulty)
    is_guess_succeeded = compare_result(guess_from_user,secret_number)
    if is_guess_succeeded:
        print(f'win you guessed :{guess_from_user} ,random number :{secret_number} ')
    else:
        print(f'lose you guessed :{guess_from_user} ,random number :{secret_number} ')



