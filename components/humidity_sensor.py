import sht
import pins

def take_reading():
    return sht.getBoth(pins.GPIO_TEMP_HUMIDITY_PIN_1, pins.GPIO_TEMP_HUMIDITY_PIN_2)

def get_humidity():
    v = take_reading()
    if v is None:
        return None
    else:
        return v[1]

def get_air_temperature():
    v = take_reading()
    if v is None:
        return None
    else:
        return v[0]

if __name__ == "__main__":
    v = take_reading()
    if v is None:
        print "error"
    else:
        print v
