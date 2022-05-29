import requests
response = requests.get("https://api.github.com/users/avielb/repos")
repos = response.json()
for repo in repos:
    print(repo["name"])