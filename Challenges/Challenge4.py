import re

def sortStringOfWords(words):
    list1 = words.split(" ")
    list1.sort(key=lambda x:x.upper())
    print(list1)
    returnString = ""
    count = 0
    for word in list1:
        returnString = "".join((returnString,word))
        count = count + 1
        if count<len(list1):
            returnString = returnString + " "
    print(returnString)

def main():

    words = input("Enter the string of words to sort")
    sortStringOfWords(words)

if __name__ == '__main__':
    main()