#PyAssistant
#A simple Program which Takes input through voice, process it , do required operations and gives the desired result.
#This assitant can do many things , and is easy to modify , only basic knowledge of python is needed.


import webbrowser as wb
import speech_recognition as sr
from tkinter import *
from time import ctime
import time
import os
from gtts import gTTS
import pygame
from pygame import mixer

def speak(audioString):
    global x
    b = audioString
    if len(b) == 0:
        #w1 = Label(root, text="No input!").pack()
        return
    tts = gTTS(text=b, lang='en-us')
    tts.save("voice%s.mp3"%(x))
    pygame.init()
    pygame.display.set_mode((2, 1))
    mixer.music.load("voice%s.mp3" % (x))
    mixer.music.play(0)

    x += 1

    clock = pygame.time.Clock()
    clock.tick(10)
    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)


def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak...")
        audio = r.listen(source)
        print("heard...")
    data = ""
 
    try:
        data = r.recognize_google(audio)
        print("You said : " + data )
        
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return data


def jarvis(data):
    if "how are you" in data:
        speak("I am fine")

    elif "what is the time" in data:
        speak(ctime())

    elif "where I am" in data:
        data = data.split(" ")
        location = data[2]
        speak("Wait a minute user, I will show you where " + location + " is.")
        wb.open_new_tab("https://www.google.nl/maps/place/" + location + "/&amp;")
    else :
        speak("I am not able get what you are saying")


time.sleep(0.5)
x=0
print("start..")
speak("Hi! User, what can I do for you?")
data = recordAudio()
jarvis(data)
speak("Turning off the program.")
print("Complete")
