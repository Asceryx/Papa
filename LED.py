import RPi.GPIO as GPIO
from utils.Captor import Captor
from utils.Board import Board
import time


def status_pin(captor):
    status_all = captor.get_input_status()
    for status in status_all:
        print("{} : {}".format(status, next(status_all)))


if __name__ == '__main__':
    b = Board(GPIO.BOARD)
    c1 = Captor({12: GPIO.OUT})
    while True:
        c1.write(12, GPIO.LOW)
        time.sleep(1)
        status_pin(c1)
        c1.write(12, GPIO.HIGH)
        status_pin(c1)
        time.sleep(1)
