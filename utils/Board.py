import RPi.GPIO as GPIO


class Board:
    """
       Initalise la carte
       mode :
              - GPIO.BOARD
              - GPIO.BCM
    """

    def __init__(self, mode):
        GPIO.setmode(mode)

    def __del__(self):
        GPIO.cleanup()

