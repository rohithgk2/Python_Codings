import random

def rollDice(firstDice,secondDice,thirdDice):
    count = int(input("How many rolls"))
    outcome = []
    probability = []
    i = 0
    while i < count:
        outcome.append((random.randint(1,firstDice)+(random.randint(1,secondDice)) + (random.randint(1,thirdDice))))
        i += 1
    values = [x for x in range(0,(firstDice+secondDice+thirdDice+1))]
    for j in values:
        if j in outcome:
            probability.append(str(round((outcome.count(j)/len(outcome))*100,2)) + "%")
        else:
            probability.append(str(0.00) + "%")
    return dict(zip(values,probability))
def main():
    firstDice = int(input("Enter the number of sides of 1st dice"))
    secondDice = int(input("Enter the number of sides of 2nd dice"))
    thirdDice = int(input("Enter the number of sides of 3rd dice"))
    print(rollDice(firstDice,secondDice,thirdDice))

if __name__ == '__main__':
    main()