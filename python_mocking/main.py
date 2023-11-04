import requests

todos_single_url = "https://jsonplaceholder.typicode.com/todos/1"
posts_url = "https://jsonplaceholder.typicode.com/posts"


def call_single_endpoint():
    request = requests.get(todos_single_url)
    return request.json()


def call_post_endpoint():
    request = requests.post(posts_url)
    return request.json()


def call_post_endpoint_with_data(data):
    request = requests.post(posts_url, data)
    return request.json()
