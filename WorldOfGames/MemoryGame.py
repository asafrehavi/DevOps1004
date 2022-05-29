import time
import common_methods
import os


def generate_sequence(length):
    sequence = []
    for index in range(int(length)):
        random_number = common_methods.generate_number(101)
        sequence.append(random_number)
    return sequence


def get_list_from_user(length):
    user_sequence = []
    for index in range(int(length)):
        guess_from_user = common_methods.get_guess_from_user(101)
        guess_int = int(guess_from_user)
        user_sequence.append(guess_int)
    return user_sequence


def wait(seconds):
    time.sleep(seconds)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def is_list_equal(generate_seq,user_seq):
    if len(generate_seq) != len(user_seq):
        return False
    for number in generate_seq:
        if number not in user_seq:
            return False
    return True


def play(difficulty):
    generate_seq = generate_sequence(difficulty)
    print(f'generated numbers :{generate_seq}')
    wait(0.7)
    clear_screen()
    user_seq = get_list_from_user(difficulty)
    is_list_equal_p = is_list_equal( generate_seq,user_seq)
    if is_list_equal_p:
        print('Win')
    else:
        print('Lost')

