from datetime import datetime
import requests


def get_rest_response(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(f"{url} is ok")

