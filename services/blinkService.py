import time
from grove.gpio import GPIO

from implementation.LedImpl import LedImpl
from system.worker import Worker


class BlinkService:
    __worker = None

    def __init__(self, led: LedImpl):
        self.isRun = False
        self._bright = led.bright
        self._light = led.measure
        self.__blink_on = 0.0
        self.__blink_off = 0.0
        self.__led = led

    def __blink(self, on, off, fade):
        self.__blink_on = on
        self.__blink_off = off
        while not self.__thr_exit:
            if fade:
                self.__led.fade_in(self.__blink_on)
                self.__led.fade_out(self.__blink_on)
            else:
                self.__led = True
                time.sleep(self.__blink_on)
                self.__led = False
                time.sleep(self.__blink_off)

    def run(self, on_time=0.5, off_time=0.5, fade=False):
        self.__worker = Worker(target=self.__blink, args=(on_time, off_time, fade))
        #self.__worker.setDaemon(True)
        self.__worker.start()
        self.isRun = True

    def stop(self):
        if self.isRun or self.__worker is not None:
            self.isRun = False
            self.__worker.join()
            self.__worker = None

    def __del__(self):
        self.stop()
