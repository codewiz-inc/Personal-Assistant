#!/usr/bin/env python3
# Requires PyAudio and PySpeech.


import speech_recognition as sr
from time import ctime
import time
import webbrowser as wb
import os
import psutil
import pyaudio
from gtts import gTTS

chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("audio.mp3")


def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        print('done!')

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        speak(("Google Speech Recognition could not understand audio"))
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data


def jarvis(data):
    if "how are you" in data:
        speak("I am fine")

    if "what time is it" in data:
        speak(ctime())

    if "where is" in data:
        data = data.split(" ")
        location = data[2:]
        print(location)
        locstr= '+'.join(location)
        print(locstr)
        speak("Hold on Boss, I will show you where it is.")
        wb.get(chrome_path).open("https://www.google.com/maps/place/" + locstr)

    if "play video on" in data:
        data = data.split(" ")
        video = data[2:]
        videostr = '+'.join(video)
        print(videostr)
        speak("Hold on ! Playing Video" )
        wb.get(chrome_path).open("https://www.youtube.com/results?search_query=" + videostr)


    if "what is my battery percentage" in data:
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = str(battery.percent)
        if plugged == False:
            plugged = "Not Plugged In"
        else:
            plugged = "Plugged In"
        bty=(percent + '% | ' + plugged)
        print(bty)
        speak(bty)

    if "search me about" in data:
        data = data.split(" ")
        search = data[2:]
        print(search)
        searchstr = '+'.join(search)
        print(searchstr)
        speak("searching,please wait"+searchstr)
        wb.get(chrome_path).open("https://www.google.co.in/search?q="+ searchstr)



# initialization
time.sleep(1)
speak("Hi Hari, what's up?")
while 1:
    data = recordAudio()
    jarvis(data)
