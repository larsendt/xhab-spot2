import spot_gpio
import pins
import sys

def set_white_lights(on):
    spot_gpio.set_pin(pins.GPIO_LIGHTS_BRIGHTNESS_PIN, on)

def set_red_lights(on):
    spot_gpio.set_pin(pins.GPIO_LIGHTS_BRIGHTNESS_PIN, on)
    spot_gpio.set_pin(pins.GPIO_RED_LIGHTS_PIN, on)

if __name__ == "__main__":
    if sys.argv[1] == "on":
        set_red_lights(True)
    elif sys.argv[1] == "off":
        set_red_lights(False)
    else:
        print "bleep bloop"
