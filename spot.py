#!/usr/bin/env python
import sys
import time

def log(*args):
    s = " ".join(map(str, args))
    print s
    with open("/home/xhab/xhab-spot/spot.log", "a") as f:
        f.write(s + "\n")

def cf(val, _min, _max):
    v = float(val)
    if v > _max or v < _min:
        raise ValueError("Value %s is out of range (%s, %s)" % (v, _min, _max))
    else:
        return v

def sbool(v):
    if v == "True" or v == "true":
        return True
    elif v == "False" or v == "false":
        return False
    else:
        raise ValueError("Value must be 'True' or 'False' (was '%s')" % v)


CFG_KEYS = {"set_air_temp_low":float, "set_air_temp_high":float,
            "set_water_temp_low":float, "set_water_temp_high":float,
            "set_rh_low":lambda x: cf(x, 0, 100), "set_rh_high":lambda x: cf(x, 0, 100),
            "set_ec_low":float, "set_ec_high":float,
            "set_ph_low":lambda x: cf(x, 0, 14), "set_ph_high":lambda x: cf(x, 0, 14),
            "set_co2_low":float, "set_co2_high":float,
            "set_do_low":float, "set_do_high":float,
            "white_light_on":sbool, "white_light_off":sbool,
            "red_light_on":sbool, "red_light_off":sbool,
            "pump_duration":float, "pump_frequency":float}

CMD_KEYS = {"fan_power":sbool, "white_light_power":sbool,
            "red_light_power":sbool, "refresh":sbool, "enclosure":sbool}

# "air_temp", "water_temp", "rh", "ec", "ph", "co2", "do",
# "name", "key", "started_on", "planted_with", "note"

def usage():
    print >> sys.stderr, "Usage: %s (command|config) <key> <value>" % sys.argv[0]


def config(key, value):
    if key in CFG_KEYS:
        try:
            v = CFG_KEYS[key](value)
            log("config:", key, v)
        except ValueError:
            log("ERROR: bad value type")
            usage()
            return -1
    else:
        log("ERROR: bad config key:", key)
        usage()
        return -1


def command(key, value):
    if key in CMD_KEYS:
        try:
            v = CMD_KEYS[key](value)
            log("command:", key, v)
        except ValueError:
            log("ERROR: bad value type")
            usage()
            return -1
    else:
        log("ERROR: bad command key:", key)
        usage()
        return -1


def main():
    if len(sys.argv) != 4:
        usage()
        return -1

    if sys.argv[1] == "config":
        return config(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "command":
        return command(sys.argv[2], sys.argv[3])
    else:
        usage()
        return -1


if __name__ == "__main__":
    main()
