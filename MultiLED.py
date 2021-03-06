import RPi.GPIO as GPIO
from dependencies.DigitalCaptor import DigitalCaptor
from dependencies.Board import Board
from system.worker import Worker
from system.csv import CSV
import time


def status_pin(captor):
    status_all = captor.get_status()
    print("--- captors pins status ----")
    for status in status_all:
        print("pin {} : {} | ".format(status, next(status_all)), end='')
    print()


def flash(count, captor, pin):
    i = 0
    current_time = time.time()
    log = []
    while i < count:
        status_pin(captor)
        captor.write(pin, not captor.read(pin))
        time.sleep(1)
        i += 1
        end = time.time() - current_time
        print("Time : {} ".format(end))
        log.append({"Captor": pin, "Time": end, "Level": captor.read(pin)})
    print("Captor pin {} : end at {}".format(pin, i))
    captor.write(pin, GPIO.LOW)
    return log


if __name__ == '__main__':
    b = Board(GPIO.BOARD)
    # Captor
    c1 = DigitalCaptor({12: GPIO.OUT})
    c2 = DigitalCaptor({16: GPIO.OUT})
    c3 = DigitalCaptor({18: GPIO.OUT})
    c4 = DigitalCaptor({22: GPIO.OUT})
    c5 = DigitalCaptor({32: GPIO.OUT})
    c6 = DigitalCaptor({36: GPIO.OUT})

    # Worker : do flashing
    w1 = Worker(target=flash, args=(10, c1, 12))
    w2 = Worker(target=flash, args=(5, c2, 16))
    w3 = Worker(target=flash, args=(3, c3, 18))
    w4 = Worker(target=flash, args=(30, c4, 22))
    w5 = Worker(target=flash, args=(12, c5, 32))
    w6 = Worker(target=flash, args=(15, c6, 36))

    # Worker : Launch work
    w1.start()
    w2.start()
    w3.start()
    w4.start()
    w5.start()
    w6.start()

    # Worker : Wait end work
    value1 = w1.join()
    value2 = w2.join()
    value3 = w3.join()
    value4 = w4.join()
    value5 = w5.join()
    value6 = w6.join()

    value = value1+value2+value3+value4+value5+value6
    c = CSV("log.csv")
    c.f_write(value[0])
    for d in value[1:]:
        c.f_append(d)
