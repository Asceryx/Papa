import time

from implementation.LedImpl import LedImpl
from models.Components import Output
from models.Led import Led
from services.blinkService import BlinkService

if __name__ == '__main__':
    pin12 = Output(channel=12)
    led = LedImpl("led", pin12, "led5v", "Led de test")
    led.light(True)
    time.sleep(1)
    led.light(False)
    blink_service = BlinkService(led)
    blink_service.run(1, 1, True)