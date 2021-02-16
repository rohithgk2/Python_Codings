import requests

def getAPI(url,resultFile):

    response = requests.request("GET",url)
    resultFile.write(response.text)
    return response.json()

def main():

    url = url = 'https://jsonplaceholder.typicode.com/albums'
    resultFile = open("results.txt", "w")
    print(getAPI(url,resultFile))

if __name__ == '__main__':
    main()