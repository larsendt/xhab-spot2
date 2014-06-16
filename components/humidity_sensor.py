import sht
import pins

def take_reading():
    return sht.getBoth(pins.GPIO_TEMP_HUMIDITY_PIN_1, pins.GPIO_TEMP_HUMIDITY_PIN_2)


if __name__ == "__main__":
    v = take_reading()
    if v is None:
        print "error"
    else:
        print v
