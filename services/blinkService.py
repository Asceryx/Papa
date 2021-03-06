import logging
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
        while self.isRun:
            if fade:
                self.__led.fade_in(self.__blink_on)
                print("[Blinking] : Fade in")
                self.__led.fade_out(self.__blink_on)
                print("[Blinking] : Fade out")
            else:
                self.__led.light(True)
                print("[Blinking] : in")
                time.sleep(self.__blink_on)
                self.__led.light(False)
                print("[Blinking] : out")
                time.sleep(self.__blink_off)

    def run(self, on_time=0.5, off_time=0.5, fade=False):
        print("[Blinking] : start working threading")
        self.__worker = Worker(target=self.__blink, args=(on_time, off_time, fade))
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
