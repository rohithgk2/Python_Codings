import re
import random

def generatePassword(count):
    with open('wordList.txt','r') as file:
        data = file.readlines()

    wordList = [line.split()[1] for line in data]

    passPhrase = [random.choice(wordList) for i in range(count)]
    return ' '.join(passPhrase)


def main():
    count = int(input("How many words to generate"))
    print(generatePassword(count))


if __name__ == '__main__':
    main()