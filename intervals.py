from datetime import time, timezone
import smbus
import GPIO
import time

sleepVar = 1


class binary(self, pins, bus):

    def __init__(self):
        self.pins = pins
        self.bus = bus

        for pin in self.pins:
            pinOn(pin, True, self.bus)
            time.sleep(sleepVar * .1)
            pinOn(pin, False, self.bus)

    def showTime(self, number):
        if number == 0:
            for pin in reversed(self.pins):
                pinOn(pin, True, self.bus)
                time.sleep(sleepVar * .1)
            for pin in reversed(self.pins):
                pinOn(pin, False, self.bus)
                time.sleep(sleepVar * .1)
        else:
            binNum = str(bin(number))
            for i, char in enumerate(binNum[-6:]):
                pinOn(self.bus, self.pins[i], int(char))


class radial(self, pins):

    def __init__(self, pins):
        self.pins = pins
        for pin in self.pins:
            pinOn(pin, True)
            time.sleep(sleepVar * .3)
        for pin in self.pins:
            pinOn(pin, False)
            time.sleep(sleepVar * .3)

    def showTime(self, hour):
        for pin in self.pins:
            pinOn(pin, True)
            time.sleep(sleepVar * .3)
        for pin in self.pins[:hour]:
            pinOn(pin, True)
            time.sleep(sleepVar * .3)
        for pin in self.pins[:hour]:
            pinOn(pin, True)
            time.sleep(sleepVar * .3)
        pinOn(self.pins[hour], True)


def pinOn(addr, tf, bus=None):
    if bus:
        bus.write_byte_data(0x40, addr, 0xff) if tf else bus.write_byte_data(
            0x40, addr, 0x00)
    else:
        GPIO.output(addr, GPIO.HIGH) if tf else GPIO.output(addr, GPIO.LOW)
