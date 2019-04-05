from datetime import time, timezone
import smbus
import RPi.GPIO as GPIO
import time

sleepVar = 0


class binary:

    def __init__(self, pins, bus):
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

            num_bits = len(self.pins)
            bits = [(number >> bit) & 1 for bit in range(num_bits - 1, -1, -1)]

            for i, bit in enumerate(bits):
                # print(bool(bit))
                pinOn(self.pins[i], bool(bit), self.bus)


class radial:

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
            pinOn(pin, False)
            time.sleep(sleepVar * .3)
        pinOn(self.pins[hour], True)


def pinOn(addr, tf, bus=None):
    if bus:
        bus.write_byte_data(0x40, addr, 0xff) if tf else bus.write_byte_data(
            0x40, addr, 0x00)
    else:
        GPIO.output(addr, GPIO.HIGH) if tf else GPIO.output(addr, GPIO.LOW)
