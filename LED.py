import RPi.GPIO as GPIO
from utils.Captor import Captor
from utils.Board import Board
import time

if __name__ == '__main__':
    b = Board(GPIO.BOARD)
    c1 = Captor({12: GPIO.IN})
    while True:
        c1.write(12, GPIO.HIGH)
        time.sleep(3)
        c1.write(12, GPIO.LOW)
