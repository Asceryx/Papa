import RPi.GPIO as GPIO
from utils import Board, Captor
import time

if __name__ == '__main__':
    b = Board(GPIO.BOARD)
    c1 = Captor({12: GPIO.IN, 14: GPIO.OUT})
    while True:
        c1.write(GPIO.HIGH)
        time.sleep(3)
        c1.write(GPIO.LOW)