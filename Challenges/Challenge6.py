
import time
import random

def gameChanger():
    targetTime = random.randint(2,5)
    input("Press enter to begin the Game")
    startTime = time.perf_counter()
    time.sleep(targetTime)
    input("Press enter to stop the game")
    endTime = time.perf_counter()
    output = endTime - startTime
    if output == targetTime:
        print("Perfect timing")
    elif output < targetTime:
        print("Short by {0:.3f} seconds".format(output-targetTime))
    else:
        print("Exceed by {0:.3f} seconds".format(output-targetTime))


def main():
    start = input("Are you ready to start the game (Y/N)")
    if start == "Y":
        print(gameChanger())
    else:
        print('Thank you')


if __name__ == '__main__':
    main()