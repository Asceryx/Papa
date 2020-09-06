from grove.gpio import GPIO

from models.Components import Output
from models.Led import Led


class LedImpl(Led):
    def __init__(self, name, pin: Output, reference, description):
        super().__init__(name, pin, reference, description)
        self.gpio = GPIO(self.pin.channel, self.pin.type)
        self._pmw = GPIO.PWM(self.pin.channel, 100)

    def turn(self, on):
        self.gpio.write(int(on))



    @property
    def bright(self):
        return super().bright

    @shutdown.setter
    def bright(self, bright):
        super(LedImpl, type(self)).bright.fset(self, bright)
        self._pwm.start(bright)

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
