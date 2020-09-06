from models.Components import Output
from models.Led import Led
from services.blinkService import BlinkService

if __name__ == '__main__':
    pin12 = Output(channel=12)
    led = Led("led", pin12, "led5v", "Led de test")
    led.shutdown = False
