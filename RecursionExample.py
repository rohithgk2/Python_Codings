
def findFactorial(x):

    if x == 1:
        return x
    else:
        return x * findFactorial(x-1)



def main():

    number = int(input("Enter the number to find its factorial"))
    print(findFactorial(number))

if __name__ == '__main__':
    main()