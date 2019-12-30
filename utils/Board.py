import RPi.GPIO as GPIO

class Board:
    """
       Initalise la carte
       mode :
              - GPIO.BOARD
              - GPIO.BCM
    """

    def __init__(mode):
        GPIO.setmode(mode)

    def getMode():
        return GPIO.getmode()

    def RAZ():
        GPIO.cleanup()