#Finding the duplicate URL
import requests

def dupURL(url,resultFile):
#My method
    response = requests.request("GET",url)
    output = response.json()
    dupUrls = []
    for value in output:
        for key,value in value.items():
            if key == 'url':
                dupUrls.append(value)
    print(len(dupUrls))
    print(len(set(dupUrls)))

#Course method
    response = requests.request("GET",url)
    output = response.json()

    urlList = []
    for value in output:
        urlList.append(value['url'])
    print(len(urlList))
    print(len(set(urlList)))

def main():

    url = "https://jsonplaceholder.typicode.com/photos"
    resultFile = open('results.txt','w')
    print(dupURL(url,resultFile))

if __name__ == '__main__':
    main()