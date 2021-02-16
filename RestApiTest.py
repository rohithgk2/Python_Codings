import requests

def getAPI():

    resultFile = open("results.txt", "w")
    url = 'https://jsonplaceholder.typicode.com/albums'
    response = requests.request("GET",url)
    resultFile.write(response.text)
    return response.json()


def main():

    print(getAPI())




if __name__ == '__main__':
    main()