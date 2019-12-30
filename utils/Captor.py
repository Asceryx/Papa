import RPi.GPIO as GPIO


class NotInitializedPin(Exception):
    pass


class Captor:
    def __init__(self, pin_setup):
        self.pin_setup = []
        for pin, status in pin_setup.items():
            GPIO.setup(pin, status)
            self.pin_setup.append(pin)

    def read(self, pin):
        if pin not in self.pin_setup:
            raise NotInitializedPin("Pin : {} is not initialized by captor".format(pin))
        else:
            return GPIO.input(pin)

    def write(self, pin, state):
        if pin not in self.pin_setup:
            raise NotInitializedPin("Pin : {} is not initialized by captor".format(pin))
        else:
            GPIO.output(pin, state)

    def get_input_status(self):
        for pin in self.pin_setup:
            yield pin
            yield self.read(pin)

    def get_output_status(self):
        for pin in self.pin_setup:
            yield pin
            yield self.read(pin)






