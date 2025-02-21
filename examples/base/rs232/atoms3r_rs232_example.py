# SPDX-FileCopyrightText: 2025 M5Stack Technology CO LTD
#
# SPDX-License-Identifier: MIT

import os, sys, io
import M5
from M5 import *
from base import AtomRS232


base_rs232 = None


def setup():
    global base_rs232

    M5.begin()
    base_rs232 = AtomRS232(
        2,
        baudrate=115200,
        bits=8,
        parity=None,
        stop=1,
        tx=5,
        rx=6,
        txbuf=256,
        rxbuf=256,
        timeout=0,
        timeout_char=0,
        invert=0,
        flow=0,
    )


def loop():
    global base_rs232
    M5.update()
    if BtnA.wasPressed():
        print("hello M5")
        base_rs232.write("hello M5")
    if base_rs232.any():
        print(base_rs232.read())


if __name__ == "__main__":
    try:
        setup()
        while True:
            loop()
    except (Exception, KeyboardInterrupt) as e:
        try:
            from utility import print_error_msg

            print_error_msg(e)
        except ImportError:
            print("please update to latest firmware")
