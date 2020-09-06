from grove.gpio import GPIO

from models.Components import Output
from models.Led import Led


class LedImpl(Led):
    def __init__(self, name, pin: Output, reference, description):
        super().__init__(name, pin, reference, description)
        self._gpio = GPIO(self.pin.channel, self.pin.type_pin)
        self._pmw = GPIO.PWM(self.pin.channel, 100)

    def turn_on(self):
        self._gpio.write(1)

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
