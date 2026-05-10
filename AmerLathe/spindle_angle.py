#!/usr/bin/env python3

import time

import hal


component = hal.component("spindle_angle")
component.newpin("revs", hal.HAL_FLOAT, hal.HAL_IN)
component.newpin("degrees", hal.HAL_FLOAT, hal.HAL_OUT)
component.ready()

try:
    while True:
        component["degrees"] = (component["revs"] * 360.0) % 360.0
        time.sleep(0.02)
except KeyboardInterrupt:
    pass
