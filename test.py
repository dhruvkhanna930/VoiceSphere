import pyttsx3                            #text to speech (install)
import speech_recognition as sr           #recognizes voice (install)
import webbrowser                         #performs web search (built-in)
import datetime                           #date and time (built-in)
import pyjokes                            #collection of python jokes over the internet
import pywhatkit
import random
import wikipedia
from bs4 import BeautifulSoup
import requests
def sptext():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio_file = r.listen(source)
        print("Time over, thank you!")
        try:
            data = r.recognize_google(audio_file)
            return data        
        except sr.UnknownValueError:
            txspeech("Sorry, didn't understood")
            return "Sorry, didn't understood"
def txspeech(text,voicemode=140):    #140 robo, 66 seductive, 136 low gossip
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate',175)
    engine.setProperty('voice', voices[voicemode].id)
    engine.say(f"{text}")
    engine.runAndWait()
mode=66
txspeech('''"beti chod", "Teri Pan Di phudich chote da lund", "madar chod", "saala", "bhen chod", "gaandu", "chuut ka patha","chhipkali ke gaand ke pasinae","tatoo ke saw daagar","randi chod", "bhen ka takka","choot ya", "randi", "bhosdi ke","bhen ke lund","Teri Ma Ki Choot"''',mode)


    
