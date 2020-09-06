from grove.gpio import GPIO
import RPi.GPIO as RPIGPIO

from models.Components import Output
from models.Led import Led

import logging


class LedImpl(Led):
    def __init__(self, name, pin: Output, reference, description):
        super().__init__(name, pin, reference, description)
        self._gpio = GPIO(self.pin.channel, self.pin.type_pin)
        self._pmw = RPIGPIO.PWM(self.pin.channel, 100)

    def light(self, status):
        self.shutdown = status
        self._gpio.write(int(status))
        if status:
            logging.info("Allumage d'une led sur le port {} ".format(self.pin.channel))
        else:
            logging.info("Extinction d'une led sur le port {} ".format(self.pin.channel))

    def fade_in(self, time):
        delay = time / 100
        for x in range(100):
            self._pmw.ChangeDutyCycle(x)
            time.sleep(delay)

    def fade_out(self, time):
        delay = time / 100
        for x in range(100, 0, -1):
            self._pmw.ChangeDutyCycle(x)
            time.sleep(delay)
