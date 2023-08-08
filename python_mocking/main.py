import requests


def call_single_endpoint():
    request = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    return request.json()


def call_post_endpoint():
    request = requests.post("https://jsonplaceholder.typicode.com/posts")
    return request.json()
