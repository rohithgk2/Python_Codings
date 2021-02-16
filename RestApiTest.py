import requests
import json

def getAPI(url,resultFile):

    response = requests.request("GET",url)
    resultFile.write(response.text)
    return response.json()

def postAPI(url,resultFile):

    payLoad = {'userId':300 , 'id':300 ,'title':'I am not giving up'}
    response = requests.request("POST", url, data=payLoad)
    resultFile.write(response.text)
    return response.json()

def putAPI(url,resultFile):

    url = '/'.join((url,'20'))
    payLoad = {'userId': 3, 'id': 20, 'title': 'I am not giving up'}
    response = requests.request("PUT",url,data=payLoad)
    resultFile.write(response.text)
    return response.json()

def deleteAPI(url,resultFile):

    url = '/'.join((url,'20'))
    response = requests.request("DELETE",url)
    resultFile.write(response.text)


def main():

    url = url = 'https://jsonplaceholder.typicode.com/albums'
    resultFile = open("results.txt", "w")
    print(getAPI(url,resultFile))
    print(postAPI(url,resultFile))
    print(putAPI(url,resultFile))
    print(deleteAPI(url,resultFile))

if __name__ == '__main__':
    main()