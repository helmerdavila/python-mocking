import docker

client = docker.from_env()


def hello_from_docker():
    containers = client.containers.list()
    images = client.images.list()
    print(containers, images)
