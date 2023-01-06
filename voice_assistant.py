import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

import pywhatkit



engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}\n")
        except Exception as e:
            print(e)
            print("Unable to Recognize your voice.")
            return None
        return query



def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        speak("Good Morning Sir !")
    
    elif hour>12 and hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    assname = "Jarvis 1 point o"
    speak("I am your Assistant")
    speak(assname)


def username():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("xxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("Welcome Mr. ", uname)
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxx")



if __name__ == '__main__':
    clear = lambda: os.system('cls')

    clear()
    wishme()
    username()

    while True:
        query = takeCommand().lower()

        if 'open youtube' in query:
            speak("Here you go to youtube\n")
            webbrowser.open("youtube.com")

        elif 'the time' in query:
            timee = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {timee}")

        elif "exit" in query:
            speak("Thanks for giving me your time")
            break

        elif "joke" in query:
            # print(pyjokes.get_joke())
            speak(pyjokes.get_joke())

        elif "whatsapp" in query:
            # print("yess")
            pywhatkit.sendwhatmsg_instantly('+91 phone number', 'Message' )

        # elif "camera" or "take a photo" in query:
        #     ec.capture(0, "Jarvis Camera", "img.png")

        # elif "WhatsApp" in query:
        #     pywhatkit.sendwhatmsg('+919752506868', 'Message by Jarvis', 0, 3)


        
