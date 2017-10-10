# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 01:47:58 2017

@author: Taelourdezzz
"""

from pyduino import *
import time
import pyttsx3
#if __name__ == '__main__':
    
a = Arduino()
    # if your arduino was running on a serial port other than '/dev/ttyACM0/'
    # declare: a = Arduino(serial_port='/dev/ttyXXXX')
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    engine.setProperty('voice',voices[1].id)
time.sleep(3)

    # sleep to ensure ample time for computer to make serial connection 
def TurnOff(pin):
    a.set_pin_mode(pin,'O')
    # initialize the digital pin as output
    time.sleep(1)
    # allow time to make connection
    x =a.digital_read(pin)
    if x == 1:
        a.digital_write(pin,0)
    else:
        engine.say("It is still turned off")
        engine.runAndWait()
    #a.close()
def TurnOn(pin):
    a.set_pin_mode(pin,'O')
    time.sleep(1)
    x =a.digital_read(pin)
    if x == 0:
        a.digital_write(pin,1)
    else:
        engine.say("It is still turned on")
        engine.runAndWait()
    #a.close()