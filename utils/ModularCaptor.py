import RPi.GPIO as GPIO
from . import Captor


class ModularCaptor(Captor):
    def __init__(self, pin_in, pin_out, pmw_channel, frequency, duty_cycle):
        Captor.__init__(self, pin_in, pin_out)
        self.pmw = GPIO.PWM(pmw_channel, frequency)
        self.pmw.start(duty_cycle)

    def write_pmw(self, frequency,  duty_cycle):
        self.pmw.ChangeFrequency(frequency)
        self.pmw.ChangeDutyCycle(duty_cycle)


