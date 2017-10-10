# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 02:29:27 2017

@author: jm
"""
import pyttsx3
import IHA_Out
engine = pyttsx3.init()
#rate = engine.getProperty('rate')
#engine.setProperty('rate', rate+10)
voices = engine.getProperty('voices')
for voice in voices:
    engine.setProperty('voice',voices[1].id)
def Lights_On(location):
   def allLights():
       print("All lights are turned on")
       engine.say('All lights are turned on')
       engine.runAndWait()
   def kitchenLights():
       print("Kitchen lights are turned on")
       IHA_Out.TurnOn(9)
       #engine.say('Kitchen lights are turned on')
       #engine.runAndWait()
   def livingRoomLights():
       print("Living room lights are turned on")
       engine.say('Living room lights are turned on')
       engine.runAndWait()
   case={"all":allLights,
         "kitchen":kitchenLights,
         "livingRoom":livingRoomLights}
   case[location]()
def Lights_Off(location):
   def allLights():
       print("All lights are turned off")
       engine.say('All lights are turned off')
       engine.runAndWait()
   def kitchenLights():
       print("Kitchen lights are turned off")
       IHA_Out.TurnOff(9)
      # engine.say('Kitchen lights are turned off')
      # engine.runAndWait()
   def livingRoomLights():
       print("Living room lights are turned off")
       engine.say('Living room lights are turned off')
       engine.runAndWait()
   case={"all":allLights,
         "kitchen":kitchenLights,
         "livingRoom":livingRoomLights}
   case[location]()
def predict(predString):
    #Get intent
    intent=predString.split('-')[0]
    #Get location
    location=predString.split('-')[1].split('=')[0]
    #Get Action
    act=predString.split('-')[1].split('=')[1]
    if intent=="lights":
        action={"on":Lights_On,
                "off":Lights_Off
                }
        action[act](location)
    if intent=="television":
        print("tv")