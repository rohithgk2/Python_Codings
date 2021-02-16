#Prime Number


def findPrimeList(index):
    count = 0
    primeList = []
    for i in range(1,11):
        # print(i)
        for j in range(1,i+1):
            if i%j==0:
                count +=1
        if count == 2:
            primeList.append(i)
        count = 0
    return primeList

def findPrimeFactors(primeList,num):
    primeFactors = []
    for i in primeList:
        while num%i == 0:
            num = num/i
            primeFactors.append(i)
    if num>1:
        primeFactors.append(int(num))
    print(primeFactors)
    
def findPrimeFactoreTheirWay(num):
    factors = []
    divisor = 2
    
    while divisor<= num:
        if num%divisor==0:
            factors.append(divisor)
            num = num/divisor
        else:
            divisor +=1
    print(factors)

def main():
    index = int(input("Enter the number upto which prime numbers are to be found"))
    num = int(input("Enter the number to find its prime factors"))
    primeList = findPrimeList(index)
    print(primeList)
    findPrimeFactors(primeList, num)
    findPrimeFactoreTheirWay(num)
if __name__ == '__main__':
    main()
