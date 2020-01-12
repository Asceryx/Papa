import RPi.GPIO as GPIO
from . import DigitalCaptor


class ModularCaptor(DigitalCaptor):
    def __init__(self, pin_in, pin_out, pmw_channel, frequency, duty_cycle):
        DigitalCaptor.__init__(self, pin_in, pin_out)
        self.pmw = GPIO.PWM(pmw_channel, frequency)
        self.pmw.start(duty_cycle)

    def write_pmw(self, frequency,  duty_cycle):
        self.pmw.ChangeFrequency(frequency)
        self.pmw.ChangeDutyCycle(duty_cycle)


