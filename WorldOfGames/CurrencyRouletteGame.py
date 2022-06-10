import requests


def get_usd_ils_value(difficulty):
    response = requests.get("https://api.exchangerate.host/convert?from=USD&to=ILS")
    t = float(response.json()["info"]["rate"])
    # lets make it more fun
    delta = ((5 - float(difficulty)) / 100)
    lower_value = t - delta
    upper_value = t + delta
    limits = {"lower": lower_value, "upper": upper_value}
    return limits


def get_rate_guess_from_user():
    try:
        user_guess = input('Enter The rate:')
        return float(user_guess)

    except ValueError:
        print('cant parse decimal')
        return 1.00


def print_result(lower, upper, guess_from_user):
    print(f'lower value :{lower} , upper value:{upper} your guess:{guess_from_user}')


def play(difficulty):
    limits = get_usd_ils_value(difficulty)
    guess_from_user = get_rate_guess_from_user()
    lower = float(limits["lower"])
    upper = float(limits["upper"])
    print_result(lower, upper, guess_from_user)
    if lower <= guess_from_user <= upper:
        print('Win')
        return True
    else:
        print('Lost')
        return False

