# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 01:47:58 2017

@author: Taelourdezzz
"""

from pyduino import *
import time

if __name__ == '__main__':
    
    a = Arduino()
    # if your arduino was running on a serial port other than '/dev/ttyACM0/'
    # declare: a = Arduino(serial_port='/dev/ttyXXXX')

    time.sleep(3)
    # sleep to ensure ample time for computer to make serial connection 

    PIN = 9
    a.set_pin_mode(PIN,'O')
    # initialize the digital pin as output
    time.sleep(1)
    # allow time to make connection
    while 1:
        y = input("pin no.?")
        if int(y) == 9:
            x =a.digital_read(PIN)
            if x == 1:
                a.digital_write(PIN,0)
            else:
                a.digital_write(PIN,1)