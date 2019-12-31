import RPi.GPIO as GPIO
from utils.Captor import Captor
from utils.Board import Board
from system.Worker import Worker
import time


def status_pin(captor):
    status_all = captor.get_status()
    for status in status_all:
        print("{} : {}".format(status, next(status_all)))


def flash(count, captor, pin):
    i = 0
    while i < count:
        status_pin(captor)
        captor.write(pin, not captor.read(pin))
        time.sleep(1)
        i += 1
    print("Captor pin {} : end at {}".format(pin, i))


if __name__ == '__main__':
    b = Board(GPIO.BOARD)
    # Captor
    c1 = Captor({12: GPIO.OUT})
    c2 = Captor({16: GPIO.OUT})
    c3 = Captor({18: GPIO.OUT})
    c4 = Captor({22: GPIO.OUT})
    c5 = Captor({32: GPIO.OUT})
    c6 = Captor({36: GPIO.OUT})

    # Worker : do flashing
    w1 = Worker(flash, 10, c1, 12)
    w2 = Worker(flash, 5, c2, 16)
    w3 = Worker(flash, 3, c3, 18)
    w4 = Worker(flash, 30, c4, 22)
    w5 = Worker(flash, 12, c5, 32)
    w6 = Worker(flash, 15, c6, 36)

    # Worker : Launch work
    w1.start()
    w2.start()
    w3.start()
    w4.start()
    w5.start()
    w6.start()

    # Worker : Wait end work
    w1.join()
    w2.join()
    w3.join()
    w4.join()
    w5.join()
    w6.join()
