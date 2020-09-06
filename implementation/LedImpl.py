import time

from grove.gpio import GPIO
import RPi.GPIO as RPIGPIO

from models.Components import Output
from models.Led import Led



class LedImpl(Led):
    def __init__(self, name, pin: Output, reference, description):
        super().__init__(name, pin, reference, description)
        self._gpio = GPIO(self.pin.channel, self.pin.type_pin)
        self._pmw = RPIGPIO.PWM(self.pin.channel, 100)
        self._pmw.start(Led.bright)

    def light(self, status):
        self.shutdown = status
        self._gpio.write(status)
        if status:
            print("Allumage d'une led sur le port {} ".format(self.pin.channel))
        else:
            print("Extinction d'une led sur le port {} ".format(self.pin.channel))

    def fade_in(self, time_in):
        delay = time_in / 100
        for x in range(100):
            self._pmw.ChangeDutyCycle(x)
            time.sleep(delay)

    def fade_out(self, time_out):
        delay = time_out / 100
        for x in range(100, 0, -1):
            self._pmw.ChangeDutyCycle(x)
            time.sleep(delay)

    def __del__(self):
        self._pmw.stop()
        RPIGPIO.cleanup()
