from enum import Enum

from models.Components import Pin


class Type(Enum):
    PRESSURE = 'pressure'
    SOUND = 'sound'
    TEMPER = 'temper'
    LIGHT = 'light'
    HUMIDITY = 'humidity'
    TOR = 'tor'


class Captor:
    def __init__(self, name, pin : Pin, reference, description):
        self.name = name
        self.reference = reference
        self.description = description
        self.pin = pin
        self.shutdown = True
        self.pause = True
        self.__measure = None

    @property
    def pause(self):
        return self.__pause

    @property
    def shutdown(self):
        return self.__shutdown

    @property
    def measure(self):
        return self.__measure

    @pause.setter
    def pause(self, pause):
        if not self.shutdown:
            self.__pause = pause
        else:
            self.__pause = True

    @shutdown.setter
    def shutdown(self, shutdown):
        if shutdown:
            self.__pause = True
        self.__shutdown = shutdown


