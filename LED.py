import RPi.GPIO as GPIO
from utils.DigitalCaptor import DigitalCaptor
from utils.Board import Board

import time


def status_pin(captor):
    status_all = captor.get_status()
    for status in status_all:
        print("{} : {}".format(status, next(status_all)))


if __name__ == '__main__':
    b = Board(GPIO.BOARD)
    c1 = DigitalCaptor({12: GPIO.OUT})
    i = 0
    while i < 10:
        status_pin(c1)
        c1.write(12, not c1.read(12))
        time.sleep(1)
        i += 1
    print("End at : {}".format(i))
