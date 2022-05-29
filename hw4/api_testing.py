import requests
import string
import random


def q1():
    url = "https://api.github.com/users/avielb/repos"
    response = requests.get(url);
    rjson = response.json()
    minimal_expected = 5
    actual = len(rjson)
    assert actual > minimal_expected


def q2():
    for x in range(3):
        S = 3  # number of characters in the string.
        # call random.choices() string module to find the string in Uppercase + numeric data.
        random_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))
        url = f"https://api.agify.io/?name={random_name}"
        response = requests.get(url);
        rjson = response.json()
        is_numeric = rjson["age"]
        assert is_numeric == 1
        age = int(rjson["age"])
        assert 0 <= age <= 120


def q3():
    url = 'http://universities.hipolabs.com/search?country=Israel'
    response = requests.get(url);
    rjson = response.json()
    minimal_expected = 5
    actual = len(rjson)
    assert actual > minimal_expected


q3()
