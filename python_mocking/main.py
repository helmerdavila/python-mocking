import requests


def call_single_endpoint():
    request = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    print(request.json())
