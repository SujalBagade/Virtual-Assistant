import pyttsx3
import requests
import speech_recognition as sr
import datetime
import os
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import sys
import time
import pyjokes
import pyautogui



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[len(voices) - 1].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#speech to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("say that again please...")
        return "none"
    return query

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour>=0 and hour<=12:
        speak(f"good morning, its {tt}")
    elif hour>12 and hour<18:
        speak(f"good afternoon, its {tt}")
    else:
        speak(f"good evening, its {tt}")
    speak("i am jarvis, sir please tell me how can i help you")


#if __name__ == "_main_":
wish()
takecommand()
while True:

        query = takecommand().lower()

        #logic builinding for tasks

        if "open notepad" in query:
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd")



        elif "play music" in query:
            music_dir =""
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak(results)
            print(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("sir,what should i search on google?")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif 'send message' in query:
            kit.sendwhatmsg("+919923588721", "this is testing protocol",2,37)

        elif "play song on youtube" in query:
            kit.playonyt("see you again")


        elif 'no thanks' in query:
            speak("thanks for using me sir , have a good day")
            sys.exit()
 #to close any application
        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn==22:
                music_dir = ''
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shutdown the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:

            os.system("rundll32.exe powrproof.dll,SetSuspendState 0,1,0")

        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "where i am" in query or "where we are" in query:
            speak("wait sir, let me check")
            try:
                ipAdd = requests.get('https://geo.ipify.org/').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                #print(geo_data)
                city = geo_data['state']
                country = geo_data['country']
                speak(f"sir i am not sure, but i think we are in {city} city of {country} country ")
            except Exception as e:
                speak("sorry sir , Due to network issue i am not able to find where we are,")
                pass


        speak("sir, do you have any other work")
