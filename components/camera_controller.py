#!/usr/bin/env python

import subprocess as sp
import time
import os
import base64

BASE_PATH = "/home/xhab/xhab-spot"

def snap_for_archive():
    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH)

    stamp = time.strftime("%Y-%m-%d_%H:%M:%S_UTC", time.gmtime())
    fname = os.path.join(BASE_PATH, "snap_" + stamp + ".jpg")
    cmd = "fswebcam -r 640x480 --no-banner -v " + fname
    retcode = sp.call(cmd.split(" "))
    if retcode == 0:
        return fname
    else:
        return None


def snap_current():
    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH)

    fname = os.path.join("/home/xhab/xhab-spot/latest.jpg")
    cmd = "fswebcam -r 640x480 --no-banner -v " + fname
    retcode = sp.call(cmd.split(" "))
    if retcode == 0:
        return fname
    else:
        return None


def latest_base64():
    with open(os.path.join("/home/xhab/xhab-spot/latest.jpg"), "rb") as f:
        data = f.read()
    return base64.b64encode(data)


if __name__ == "__main__":
    snap_current()
