#!/usr/bin/env python

import spot_gpio
import pins
import sys

def set_fans(on):
    spot_gpio.set_pin(pins.GPIO_PLANT_FAN, on)
    spot_gpio.set_pin(pins.GPIO_EPS_FAN, on)


if __name__ == "__main__":
    if sys.argv[1] == "on":
        set_fans(True)
    elif sys.argv[1] == "off":
        set_fans(False)

