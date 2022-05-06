from http import server
from importlib.resources import contents
from json.tool import main
import pyttsx3
import pyaudio
import datetime
import wikipedia 
import webbrowser # for browsing 
import os   # for music 
import smtplib

import speech_recognition as sr
from PyQt5 import QtWidgets, QtCore ,QtGui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
#print(voices[1].id)

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am System Sir....Please tell me how may I help you?")

def takeCommand():
    #It takes microphone input from the user and return string output

    r = sr.Recognizer() #it helps us to recognize audio
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 #seconds of non-speaking audio before a phrase is considered complete   bolanyat gap ala tar to gap 1 second cha consider karayacha
        audio = r.listen(source,timeout=1,phrase_time_limit=5)

# def takeCommand():
#     #It takes microphone input from the user and returns string output

#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         print("I'm listening...")
#         audio = r.listen(source)

        try:
            print("Recognizing...") 
            
            query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
            
            print(f"User said: {query}\n")  #User query will be printed.

        except Exception as e:
            # print(e)    
            print("Say that again please...")   #Say that again will be printed in case of improper voice 
            return "None" #None string will be returned
        return query
# def sendmail(to, content):
#              server = smtplib.SMTP('SMTP.gmail.com', 587)
#              server.ehlo()
#              server.starttls()
#              server.login('youremail@gmail.com','your-password')
#              server.sendmail('yourmail@gmail.com',to,content)
#              server.close()

if __name__ == "main_":
    speak("Hello vaibhav, How are you?")
    WishMe()
    if 1:
        query=takeCommand().lower()
    # LOgic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        

        elif 'play music' in query:
            music_dir='C:\\Users\my pici\\Music\\music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[1]))

        elif 'the date and time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S:%DD:%MM:%YYYY")
            speak(f"Sir, the time and date{strTime}")

        # elif 'the date' in query:
        #     strDate=datetime.datetime.now().strfDate("%DD:%MM:%YYYY")
        #     speak(f"Sir, the date is {strDate}")
        elif 'open map' in query:
             webbrowser.open("maps.google.com")
            
        elif  'todays weather ' in query:
             webbrowser.open("weather.google.com")

       


        
        # elif 'email to vaibhav' in query:
        #     try:
        #         speak('what should i say')
        #         content=takeCommand()
        #         to="shelkev2001@gmail.com"
        #         sendmail(to,content)
        #         speak("Email has been sent...")
        #     except Exception as e:
        #         print("Sending mail...")
            
    # if quit in query:
    #     exit()