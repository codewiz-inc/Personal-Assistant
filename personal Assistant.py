import speech_recognition as sr
from time import ctime
import time
import sys
import webbrowser as wb
import os
import psutil
import pyaudio
import subprocess as sp
from gtts import gTTS
import urllib
from urllib.request import urlopen
from urllib.parse import quote
import urllib.parse
from bs4 import BeautifulSoup
import fnmatch

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
        #speak(("Google Speech Recognition could not understand audio"))
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data


def shaz(data):
    if "how are you" in data:
        speak("I am fine")

    if "what time is it" in data:
        speak(ctime())

    if "open Notepad" in data:
        programName = "notepad.exe"
        sp.Popen([programName])

    if "open calculator" in data:
        programName = "C:\Windows\System32\calc.exe"
        sp.Popen([programName])


    if "where is" in data:
        data = data.split(" ")
        location = data[2:]
        print(location)
        locstr= '+'.join(location)
        print(locstr)
        speak("Hold on, I will show you where it is.")
        wb.get(chrome_path).open("https://www.google.com/maps/place/" + locstr)


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
        search = data[3:]
        print(search)
        searchstr = '+'.join(search)
        print(searchstr)
        speak("searching,please wait")
        wb.get(chrome_path).open("https://www.google.co.in/search?q="+ searchstr)

    if "play video on" in data:
        list=[]
        data = data.split(" ")
        video = data[3:]
        print(video)
        videostr = ' '.join(video)
        print(videostr)
        query = urllib.parse.quote(videostr)
        url = "https://www.youtube.com/results?search_query=" + query
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html)
        for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
            list.append('https://www.youtube.com' + vid['href'])

        print(list[0])
        wb.get(chrome_path).open(list[0])


    if "open Facebook" in data:
        speak("please wait until your browser will open")
        wb.get(chrome_path).open("https://www.facebook.com/")


    if "open Twitter" in data:
        speak("please wait until your browser will open")
        wb.get(chrome_path).open("https://twitter.com/")



    if "open LinkedIn" in data:
        speak("please wait until your browser will open")
        wb.get(chrome_path).open("https://www.linkedin.com/")



    if "open Gmail" in data:
        speak("please wait until your browser will open")
        wb.get(chrome_path).open("https://mail.google.com/")

    if "Run" in data or "run" in data:
        data = data.split(" ")
        openpro = data[1:]
        print(openpro)
        openstr=' '.join(openpro)
        drives = ['C:\\', 'D:\\', 'E:\\', 'F:\\']
        pattern = (openstr+".exe")
        print(pattern)
        filelist = []
        with open("log.txt", "wb") as fs:
            for rootPath in drives:
                print("Now searching in: ", rootPath)
                for root, dirs, files in os.walk(rootPath):
                    for filename in fnmatch.filter(files, pattern):
                        filepath = os.path.join(root, filename)
                        print(filepath)
                        filelist.append(filepath)
                        print(filelist)
                        result = os.path.join(root, filename)
                        fs.write(bytearray((result + "\n"), 'utf8'))

        print(filelist[0])
        os.startfile(filelist[0])

    if "exit" in data or "Thank you" in data:
        sys.exit()

time.sleep(1)
speak("Hi dude, what's up?")
while 1:
    data= recordAudio()
    shaz(data)
