#!/usr/bin/env python

def get_pin(pin):
    fname = "/proc/adc" + str(pin)
    with open(fname, "r") as f:
        val = int(f.read()[5:-1])
    return val

