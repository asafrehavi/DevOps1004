import MemoryGame
import GuessGame
import CurrencyRouletteGame
from Live import validate


def get_game_level():
    level_message = 'Please choose game difficulty from 1 to 5:'
    is_level_valid = False
    level = 1
    while not is_level_valid:
        level = input(level_message)
        is_level_valid = validate(level, 1, 5, 'game level is not valid')
    return level


def get_game_number():
    choose_game_message = """Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to
    guess it back
    2. Guess Game - guess a number and see if you chose like the computer
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS
    """

    is_game_valid = False
    while not is_game_valid:
        game_number = input(choose_game_message)
        is_game_valid = validate(game_number, 1, 3, 'cant find this game')
        if is_game_valid:
            return game_number;


def validate(value, low, high, failure_message):
    value_string = str(value)
    if not value_string.isdigit():
        print(failure_message)
        return False
    value = int(value)
    if high >= value >= low:
        return True
    print(failure_message)
    return False


def welcome(name):
    return f'Hello {name} and welcome to the World of Games (WoG). Here you can find many cool games to play.'


def load_game():
    game_number = get_game_number()
    level = get_game_level()
    if game_number == '1':
        MemoryGame.play(level)
    if game_number == '2':
        GuessGame.play(level)
    if game_number == '3':
        CurrencyRouletteGame.play(level)


load_game()
