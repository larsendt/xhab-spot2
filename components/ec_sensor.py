import spot_gpio
import spot_analog
import pins
import time

def take_reading():
    gpin = pins.GPIO_EC_PIN
    ec_apin = pins.ADC_EC_PIN
    temp_apin = pins.ADC_WATER_TEMP_PIN
    tempval = 0
    ecval = 0
    for i in range(10):
        time.sleep(0.5)
        spot_gpio.set_pin(gpin, True)
        time.sleep(0.01)
        ec = spot_analog.get_pin(ec_apin)
        temp = spot_analog.get_pin(temp_apin)
        time.sleep(0.49)
        spot_gpio.set_pin(gpin, False)

        # really unsure about this part
        # I don't know why we're throwing away successive readings
        # is it waiting for the value to stabilize or something?
        tempval = (0.0000060954 * pow(temp,2)) + (0.00690983 * temp) + 20.9983
        ecval = (0.0023 * pow(ec,2)) - (12.6 * ec) + 17520.1
    return tempval, ecval

def get_water_temperature():
    return take_reading()[0]

def get_ec():
    return take_reading()[1]
