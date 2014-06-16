#!/usr/bin/env python

import pins
import time
import spot_gpio
import sys

ROTATE_TIME = 7

def rotate(pin, r_time):
    spot_gpio.set_pin(pin, True)
    start = time.time()
    while time.time() - start > r_time:
        pass
    spot_gpio.set_pin(pin, False)


def rotate_left():
    rotate(pins.GPIO_ROTATION_LEFT, ROTATE_TIME)


def rotate_right():
    rotate(pins.GPIO_ROTATION_RIGHT, ROTATE_TIME)


if __name__ == "__main__":
    t = float(sys.argv[2])
    if sys.argv[1] == "left":
        rotate(pins.GPIO_ROTATION_LEFT, t)
    elif sys.argv[1] == "right":
        rotate(pins.GPIO_ROTATION_RIGHT, t)
    else:
        print "bleep bloop"
