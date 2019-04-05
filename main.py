import RPi.GPIO as GPIO
import smbus
import time
import datetime as dt
from intervals import radial, binary


minAddr = [0x01, 0x02, 0x03, 0x04, 0x05, 0x06]
secAddr = [0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d]
hourPin = [7, 8, 10, 11, 12, 13, 15, 16,
           18, 19, 21, 22, 23, 24, 26, 29, 31, 32, 33, 35, 36, 37, 38, 40]


def startup():
    GPIO.setmode(GPIO.BOARD)

    for pin in hourPin:
        GPIO.setup(pin, GPIO.OUT)

    bus = smbus.SMBus(1)

    h = radial(hourPin)
    m = binary(minAddr, bus)
    s = binary(secAddr, bus)

    return h, m, s

if __name__ == '__main__':
    oldHour = 100
    oldMinute = 100
    oldSecond = 100

    h, m, s = startup()

    while True:

        currentTime = dt.datetime.now().time()
        currentHour = currentTime.hour
        currentMinute = currentTime.minute
        currentSecond = currentTime.second

        if currentHour != oldHour:
            print(currentHour)
            h.showTime(currentHour)
            oldHour = currentHour
            oldSecond = dt.datetime.now().time().second
            s.showTime(oldSecond)
        if currentMinute != oldMinute:
            print(currentMinute)
            m.showTime(currentMinute)
            oldMinute = currentMinute
        if currentSecond != oldSecond:
            print(currentSecond)
            s.showTime(currentSecond)
            oldSecond = currentSecond
