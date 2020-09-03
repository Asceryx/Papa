import time
from grove.gpio import GPIO
from models.Led import Led
from system.worker import Worker


class BlinkService:
    def __init__(self, led: Led):
        self.isRun = False
        self._bright = led.bright
        self._light = led.measure
        self.__blink_on = 0.0
        self.__blink_off = 0.0
        self.__gpio = GPIO(led.pin.channel, led.pin.type)
        self.__worker = None

    def __lighton(self, b=True):
        v = self._light == bool(b) and bool(self._bright)
        self.__gpio.write(int(v))

    def __blink(self, on=0.5, off=0.5):
        self.__blink_on = on
        self.__blink_off = off
        while not self.__thr_exit:
            self.__lighton(True)
            time.sleep(self.__blink_on)
            self.__lighton(False)
            time.sleep(self.__blink_off)

    def run(self, on_time=0.5, off_time=0.5):
        self.__worker = Worker(target=self.__blink, args=(on_time, off_time))
        self.__worker.setDaemon(True)
        self.__worker.start()
        self.isRun = True

    def stop(self):
        if self.isRun or self.__worker is not None:
            self.isRun = False
            self.__worker.join()
            self.__worker = None

    def __del__(self):
        self.stop()
