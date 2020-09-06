from implementation.LedImpl import LedImpl
from models.Components import Output
from models.Led import Led
from services.blinkService import BlinkService

if __name__ == '__main__':
    pin17 = Output(channel=17)
    led = LedImpl("led", pin17, "led5v", "Led de test")
    led.turn_on()