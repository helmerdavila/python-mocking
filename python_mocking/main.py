import requests


def hello_from_docker():
    request = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    print(request.json())
