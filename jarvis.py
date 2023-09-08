import random
import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning daa")
    elif hour >=12 and hour <18:
        speak("Good Afternoon daa")
    else:
        speak("Good Evening daa")
    speak("Ninde paree Jarvis, entha para?")
    
def takeCommand():
    # takes mic input from user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1.5
        audio=r.listen(source)
        
        
    try:
        print("Recongizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please....")
        return "none"
    return query
   
if __name__=='__main__':
    wishMe() 
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
          speak('Searching Wikipedia...')
          query= query.replace("wikipedia"," ")
          results=wikipedia.summary(query,sentences=2)
          speak("According to what I know")
          speak(results)
          print(results)
        elif 'open youtube ' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'cinema' in query:
            webbrowser.open("smashystreams.xyz")
        elif 'sangeetam' or 'music' in query:
            music_dir='C:\\Users\\aditi\\OneDrive\\Desktop\\songs'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[random.randint(0,len(songs)-1)]))
        elif 'samay' or 'time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"eppol samayam {strTime}")
        elif 'open code' or 'vscode'in query:
            codePath="C:\\Users\\aditi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'gmail' in query:
            webbrowser.open("gmail.com")
        elif 'hungry' in query:
            webbrowser.open("swiggy.com")
        elif 'shopping' in query:
            webbrowser.open("amazon.in")
        elif 'advice' in query:
            speak("Sure, here's a piece of advice: 'Stay positive and never give up on your dreams.'")
        elif 'amrita' in query:
            speak("pooda pattti, paanni, thaendii, naarrii")
        elif 'bored' or 'boring' in query:
            webbrowser.open("https://www.youtube.com/shorts/")
        elif 'quit' in query:
            exit()
        elif 'shukran' in query:
            exit()
        elif 'bye' in query:
            exit()
        elif 'sheri' in query:
            exit()     