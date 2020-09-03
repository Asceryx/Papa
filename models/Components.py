try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this "
          "by using 'sudo' to run your script")

MODE = "BCM"
GPIO.setmode(MODE)


class Pin:
    type = None

    def __init__(self, channel, initial):
        self.channel = channel
        self.initial = initial


class Input(Pin):
    type = GPIO.IN

    def __init__(self, channel, initial=GPIO.HIGH, default=0):
        self.value = default
        super().__init__(channel, initial)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self):
        self.__value = GPIO.input(self.channel)


class Output(Pin):
    type = GPIO.OUT

    def __init__(self, channel, initial=GPIO.HIGH, default=0):
        self.state = default
        super().__init__(channel, initial)

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        GPIO.output(self.channel, state)
        self.__state = state


class Rpi:
    p1_revision = GPIO.RPI_INFO['P1_REVISION']
    ram = GPIO.RPI_INFO['RAM']
    revision = GPIO.RPI_INFO['REVISION']
    type = GPIO.RPI_INFO['TYPE']
    processor = GPIO.RPI_INFO['PROCESSOR']
    manufacturer = GPIO.RPI_INFO['MANUFACTURER']


class Board(Rpi):
    def __init__(self, pins):
        self.__pinInput = {}
        self.__pinOutput = {}
        for pin in pins:
            GPIO.setup(pin.channel, pin.input_status, pin.initial)
            if pin.type == GPIO.OUT:
                self.__pinOutput[pin.channel] = pin
            elif pin.type == GPIO.IN:
                self.__pinInput[pin.channel] = pin

    def getAllState(self):
        return self.__pinInput

    def getState(self, channel):
        return self.__pinInput[channel].value

    def setState(self, channel, state):
        if channel in self.__pinOutput:
            self.__pinOutput[channel].state = state

    def __del__(self):
        GPIO.cleanup()
