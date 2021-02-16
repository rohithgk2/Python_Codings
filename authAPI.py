import json
import requests

def gitApi(url):

    headers = {'Authorization':'Bearer ab405186fc5c9c06fb66ca7846f254c1006935e5'}
    response = requests.request("GET",url,headers=headers)
    return response.json()


def main():

    url = "https://api.github.com/user/repos"
    print(gitApi(url))


if __name__ == '__main__':
    main()