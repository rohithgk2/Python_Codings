import re

def checkPalindrome(word):
    #Remove whitespaces
    word = word.replace(" ","")

    #Changing all case to lower
    word = word.lower()

    if word[::-1] == word:
        return True
    else:
        return False


def main():

    word = input("Enter the word to check Palindrome")
    print(checkPalindrome(word))

if __name__ == '__main__':
    main()