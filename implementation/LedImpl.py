from grove.gpio import GPIO
import RPi.GPIO as RPIGPIO

from models.Components import Output
from models.Led import Led


class LedImpl(Led):
    def __init__(self, name, pin: Output, reference, description):
        super().__init__(name, pin, reference, description)
        self._gpio = GPIO(self.pin.channel, self.pin.type_pin)
        self._pmw = RPIGPIO.PWM(self.pin.channel, 100)

    def turn_on(self):
        self.shutdown = False
        self._gpio.write(1)

    def turn_off(self):
        self.shutdown = True
        self._gpio.write(0)

    def fade_in(self, time):
        delay = time / 100
        for x in range(100):
            self._pwm.ChangeDutyCycle(x)
            time.sleep(delay)

    def fade_out(self, time):
        delay = time / 100
        for x in range(100, 0, -1):
            self._pwm.ChangeDutyCycle(x)
            time.sleep(delay)
