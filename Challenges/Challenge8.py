import playsound
import time
import datetime

def setAlarm():

    alarmTime = int(input("How much seconds  after to ring alarm"))
    print("Alarm set for {}".format(datetime.datetime.now()+datetime.timedelta(seconds=alarmTime)))
    time.sleep(alarmTime)
    print("Wake UP")
    playsound.playsound('C:/Users/rohit/Downloads/ALARMCLOCK.wav')


def main():

    setAlarm()

if __name__ == '__main__':
    main()
