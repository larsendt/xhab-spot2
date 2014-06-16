#!/usr/bin/env python
import sys
import time
import components
import json


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


def ntype(v):
    return v


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
            "red_light_power":sbool, "refresh":sbool, "enclosure":sbool,
            "take_picture":ntype}

# "air_temp", "water_temp", "rh", "ec", "ph", "co2", "do",
# "name", "key", "started_on", "planted_with", "note"


def do_config(key, value):
    d = {"message":"config %s is not yet implemented" % key,
         "data":None,
         "error":False}
    print json.dumps(d)


def config(key, value):
    if key in CFG_KEYS:
        try:
            v = CFG_KEYS[key](value)
        except ValueError:
            d = {"message":"Bad value type for key '%s'" % key,
                 "data":None,
                 "error":True}
            print json.dumps(d)
            return -1
    else:
        d = {"message":"Bad key '%s'" % key,
             "data":None,
             "error":True}
        print json.dumps(d)
        return -1


def do_command(key, value):
    if key == "take_picture":
        data = components.camera_controller.latest_base64()
        d = {"message":"took a picture", "error":False, "data":data}
        print json.dumps(d)
    else:
        d = {"message":"command %s is not yet implemented" % key,
             "data":None,
             "error":False}
        print json.dumps(d)


def command(key, value):
    if key in CMD_KEYS:
        try:
            v = CMD_KEYS[key](value)
            do_command(key, v)
        except ValueError:
            d = {"message":"Bad value type for key '%s'" % key,
                 "data":None,
                 "error":True}
            print json.dumps(d)
            return -1
    else:
        d = {"message":"Bad key '%s'" % key,
             "data":None,
             "error":True}
        print json.dumps(d)
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
        d = {"message":"bad input %s, expected 'config' or 'command'" % sys.argv[1],
             "data":"",
             "error":True}
        print json.dumps(d)
        return -1


if __name__ == "__main__":
    main()
