import time
import smbus2 as smbus
from smbus2 import i2c_msg

ADC_DEFAULT_IIC_ADDR = 0X04

ADC_CHAN_NUM = 8

REG_RAW_DATA_START = 0X10
REG_VOL_START = 0X20
REG_RTO_START = 0X30

REG_SET_ADDR = 0XC0


class Bus:
    instance = None
    MRAA_I2C = 0

    def __init__(self, bus=None):
        if bus is None:
            try:
                import RPi.GPIO as GPIO
                # use the bus that matches your raspi version
                rev = GPIO.RPI_REVISION
            except:
                rev = 3
            if rev == 2 or rev == 3:
                bus = 1  # for Pi 2+
            else:
                bus = 0
        if not Bus.instance:
            Bus.instance = smbus.SMBus(bus)
        self.bus = bus
        self.msg = i2c_msg

    def __getattr__(self, name):
        return getattr(self.instance, name)


class AnalogCaptor:
    def __init__(self, bus_num=1, addr=ADC_DEFAULT_IIC_ADDR, pin_setup=[]):
        self.bus = Bus(bus_num)
        self.addr = addr
        self.pin = pin_setup

    def read(self, pin):
        data = self.bus.read_i2c_block_data(self.addr, REG_RAW_DATA_START + pin, 2)
        val = data[1] << 8 | data[0]
        return val

    def read_all(self):
        value_array = []
        for n in self.pin:
            val = self.read(n)
            value_array.append(val)
        return value_array

    def write(self, pin, data):
        self.bus.read_i2c_block_data(self.addr, REG_RAW_DATA_START + pin, data)

    def write_all(self, pin, data):
        for n in self.pin:
            self.write(n, data)
