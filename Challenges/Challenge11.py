import re
from collections import Counter
def countWords():
    flag = 0
    with open('input.txt','r') as file:
        data = file.readlines()
        wordList = []
        wordCount = []

    for word in data:
        word = (re.findall('[\w]+', word))
        wordList = wordList + word
    print("Total words: " , len(wordList))

    wordCounter = Counter()

    for element in wordList:
        wordCounter[element] += 1
    print(wordCounter)

    print("Top 20 words:\n")
    for word in wordCounter.most_common(20):
        print(word[0] , ":" , word[1])

    for element in wordList:
        count = wordList.count(element)
        wordCount.append(count)
    finalDict = dict(zip(wordList,wordCount))

    finalSortedDict = sorted(finalDict,key=finalDict.get , reverse=True)
    print("The top words are given below \n")
    for i in finalSortedDict:
        print(i,finalDict[i])
        flag +=1
        if flag == 10:
            break

def main():

    countWords()


if __name__ == '__main__':
    main()