#!/usr/bin/env python

import pins
import time
import spot_gpio
import sys

GPIO_DOOR_MOTOR_OPEN = 14
GPIO_DOOR_MOTOR_CLOSE = 15

ROTATE_TIME = 7

def rotate(pin, r_time):
    spot_gpio.set_pin(pin, True)
    start = time.time()
    while time.time() - start > r_time:
        pass
    spot_gpio.set_pin(pin, False)


def open_curtain():
    rotate(pins.GPIO_DOOR_MOTOR_OPEN, ROTATE_TIME)


def close_curtain():
    rotate(pins.GPIO_DOOR_MOTOR_CLOSE, ROTATE_TIME)


if __name__ == "__main__":
    t = float(sys.argv[2])
    if sys.argv[1] == "open":
        rotate(pins.GPIO_DOOR_MOTOR_OPEN, t)
    elif sys.argv[1] == "close":
        rotate(pins.GPIO_DOOR_MOTOR_CLOSE, t)
    else:
        print "bleep bloop"
