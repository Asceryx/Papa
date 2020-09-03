from models.Captor import Captor, Type
from models.Components import Output


class Led(Captor):
    MAX_BRIGHT = 100

    def __init__(self, name, pin: Output, reference, description):
        super().__init__(name, pin, reference, description)
        self.__light = False
        self.__bright = 0
        self.type = Type.TOR

    @property
    def shutdown(self):
        return super().shutdown

    @property
    def measure(self):
        return self.__light

    @property
    def bright(self):
        return self.__bright

    @shutdown.setter
    def shutdown(self, shutdown):
        super(Led, type(self)).shutdown.fset(self, shutdown)
        brightness = {True: 0, False: self.MAX_BRIGHT}
        self.__light = not shutdown
        self.__bright = brightness[shutdown]

    @bright.setter
    def bright(self, bright):
        if bright <= 0 or self.shutdown:
            self.__bright = 0
        elif bright >= self.MAX_BRIGHT and not self.shutdown and not self.pause:
            self.__bright = self.MAX_BRIGHT
        elif not self.shutdown and not self.pause:
            self.__bright = bright


if __name__ == "__main__":
    c = Captor("Toto", 11, "POIUYT", "C'est un capteur")
    l = Led("led", 12, "AZERTY", "Ceci n'est pas une led")

    l.pause = False
    l.bright = 50
    l.bright = 190
    l.shutdown = False
    l.bright = 50
    l.bright = 190
    print(l.shutdown, l.pause)