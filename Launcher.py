import time

from implementation.LedImpl import LedImpl
from models.Components import Output
from models.Led import Led
from services.blinkService import BlinkService

if __name__ == '__main__':
    pin18 = Output(channel=18)
    led = LedImpl("led", pin18, "led5v", "Led de test")
    led.light(True)
    time.sleep(10)
    led.light(False)
    blink_service = BlinkService(led)
    blink_service.run(1, 1, False)