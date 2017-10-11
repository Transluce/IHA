# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 23:08:16 2017

@author: Taelourdezzz
"""
import winsound
from datetime import datetime
alldate = ""
alarm = input("Time to do alarm? [HH:MM:SS]")
while alarm != alldate:
    alldate = str(datetime.now().strftime("%H:%M:%S"))
print("Time is already " + alldate)
x = True
winsound.PlaySound("creep.wav", winsound.SND_ASYNC)
while x == True:
    stop = input("you want to stop?")
    if (stop == "yes"):
        x = False
        winsound.PlaySound(None, winsound.SND_PURGE)