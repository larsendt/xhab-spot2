#!/usr/bin/env python

import json
import subprocess as sp
import shlex
import re
import sys
import components

URL = "http://192.168.43.94:3000/spots/1"
CMD = "curl -silent -output /dev/null -H \"Accept: application/json\" -H \"Content-type: application/json\" -X PATCH -d '%s' %s"
SENSORS = ["air_temp", "water_temp", "rh", "ec", "ph", "co2", "do", "water_level",
           "battery_level"]

def send_patch(data):
    print data
    s = json.dumps(data)
    p = sp.Popen(shlex.split(CMD % (s, URL)), stdout=sp.PIPE, stderr=sp.PIPE)
    ret = p.wait()
    out = p.stdout.read()
    retcode, retstr = re.findall(r"HTTP/1\.1 (\d+) (.*)\r", out)[0]
    if retcode != "200":
        print retcode, retstr

CACHE = {}
def get_reading(sensor):
    if sensor in CACHE:
        return CACHE[sensor]
    elif sensor == "air_temp":
        print "Reading air temp"
        CACHE["air_temp"], CACHE["rh"] = components.humidity_sensor.take_reading()
        return CACHE["air_temp"]
    elif sensor == "water_temp":
        print "Reading water temp"
        CACHE["water_temp"], CACHE["ec"] = components.ec_sensor.take_reading()
        return CACHE["water_temp"]
    elif sensor == "rh":
        print "Reading relative humidity"
        CACHE["air_temp"], CACHE["rh"] = components.humidity_sensor.take_reading()
        return CACHE["rh"]
    elif sensor == "ec":
        print "Reading EC"
        CACHE["water_temp"], CACHE["ec"] = components.ec_sensor.take_reading()
        return CACHE["ec"]
    elif sensor == "ph":
        print "Reading pH"
        CACHE["ph"] = components.ph_sensor.get_ph()
        return CACHE["ph"]
    elif sensor == "co2":
        print "Reading CO2"
        CACHE["co2"] = components.co2_sensor.take_reading()
        return CACHE["co2"]
    elif sensor == "do":
        print "Reading CO"
        CACHE["do"] = components.do_sensor.take_reading()
        return CACHE["do"]
    elif sensor == "water_level":
        print "Reading water level"
        CACHE["water_level"] = components.water_level_sensor.take_reading()
        return CACHE["water_level"]
    elif sensor == "battery_level":
        print "Reading battery level"
        CACHE["battery_level"] = components.battery_sensor.battery_level()
        return CACHE["battery_level"]
    else:
        return 1e9


def main():
    data = {}
    sensors = sys.argv[1:]
    if not sensors:
        sensors = SENSORS

    for sensor in sensors:
        if sensor in SENSORS:
            reading = get_reading(sensor)
            data[sensor] = reading
        else:
            print "No such sensor:", sensor
    print send_patch({"spot":data})

if __name__ == "__main__":
    main()

