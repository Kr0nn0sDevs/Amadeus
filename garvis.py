from numpy import take
import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui #pip install pyautogui
import psutil #pip install psutil
import pyjokes #pip install pyjokes
import pywhatkit as kit #pip install pywhatkit
from time import sleep
#install: pip install pipwin, pipwin install pyaudio
#Instalar el archivo de python que esta en la carpeta del proyecto (PyAudio)
#Revisar luego lo de spotify
# import openspotify

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    elif hour >= 18 and hour < 24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(day)
    speak(month)
    speak(year)
    
def wishme():
    #speak("Welcome back Sir!!")
    #time()
    #date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good Morning Sir!!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!!")
    elif hour >= 18 and hour < 24:
        speak("Good Evening Sir!!")
    else:
        speak("Good Night Sir!!")
    speak("Jarvis at your service plaese tell me how can i help you?")

def takeComand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening .... ")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizning .... ")
        query = r.recognize_google(audio, language='en-in')
        print(query)
            
    except Exception as e:
        print(e)
        speak("Say that again please ....")
        
        return "None"
        
    return query

def sendEmail(to, content): # Revisar luego el envio de emails
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('chrosiland003@gmail.com', 'droviland003')
    server.sendmail('chrosiland003@gmail.com',to, content)
    
def screenshot():
    img = pyautogui.screenshot('unamed.jpg')

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)
    battery = psutil.sensors_battery()
    speak("batery is at")
    speak(battery.percent)
    
def jokes():
    speak(pyjokes.get_joke())

def message():
    speak("Tell me the phone of contact")
    contact = takeComand().lower()
    
    wb.open('https://web.whatsapp.com/send?phone=+529671269131'    """Poner un +contact despues de las comillas luego""")
    
    sleep(10)
    
    speak("Which is your message?")
    mesage = takeComand().lower()
    for i in range(12):
        pyautogui.press('tab')
    
    pyautogui.typewrite("My name is Amadeus, i am virtual assistant for Christain, he is send this message")
    pyautogui.press('enter')
    pyautogui.typewrite(mesage)
    pyautogui.press('enter')
    
def song():
    speak("What's name of song?")
    song = takeComand().lower()
    kit.playonyt(song)

def spotify():
    speak("What's tour command?")
    song = takeComand().lower()
    #speak("The author?")
    #author = takeComand()
    client_id = 'cfb218957763498c844689eeeab8fe9e'
    secret_id = '0ee26d50dade4d69bb99661a1f53b198'
    flag = 0
    if flag == 0:
        song = song.replace(" ", "%20")
        wb.open(f'spotify:search:{song}')
        sleep(5)
        flag = 1
        for i in range(28):
            pyautogui.press("tab")

        for i in range(1):
            pyautogui.press("enter")
            sleep(1)
    #Revisar esto luego, es para nueva busqueda de cancion, necesito cambios
    """if flag == 1:
        song = song.replace(" ", "%20")
        wb.open(f'spotify:search:{song}')
        sleep(5)
        flag = 1
        for i in range(27):
            pyautogui.press("tab")
            
        for i in range(1):
            pyautogui.press("enter")
            sleep(1)"""         

    """if len(author) > 0:
        # authenticate
        sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, secret_id))
        result = sp.search(author)
        
        for i in range(0, len(result["tracks"]["items"])):
            # songs by artist
            name_song = result["tracks"]["items"][i]["name"].upper()
            
            if song in name_song:
                flag = 1
                wb.open(result["tracks"]["items"][i]["uri"])
                sleep(5)
                pyautogui.press("enter")
                break"""

    # Searching song
    """if 'search' in command:
        speak("Whats searching song?")
        song = takeComand().lower()
        track = song.upper()
        if flag == 0:
            songs = track.replace(" ", "%20")
            wb.open(f'spotify:search:{songs}')
            sleep(5)
            for i in range(29):
                pyautogui.press("tab")

            for i in range(1):
                pyautogui.press("enter")
                sleep(1)"""
    #playlists
    """elif 'like' in command:
        wb.open(f'spotify:')
        sleep(5)
        for i in range(1):
            pyautogui.press('enter')
        
        for i in range(5):
            pyautogui.press('tab')
        
        for i in range(1):
            pyautogui.press('enter')"""
    
if __name__ == "__main__":
    wishme()
    while True:
        query = takeComand().lower()
        
        if 'time' in query:
            time()
        
        elif 'your name' in query:
            speak("My name is Jarvis sir!")#Nombre provicional
        
        elif 'date' in query:
            date()
            
        elif 'thanks' in query:
            speak("Sure sir!")
        
        elif 'wikipedia' in query:
            speak("searching....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        
        elif 'send email' in query:     # Revisar luego el envio de Emails
            try:
                speak("What should I Say?")
                content = takeComand()
                to = 'chrosiland@gmail.com'
                sendEmail(to, content)
                speak(content)
            except Exception as e:
                print(e)
                speak("Uable to send your email")
        
        #Busqueda primaria
        #elif 'search in firefox' in query:
        #    speak("What should i search ?")
        #    firefoxpath = '/lib/firefox-esr/firefox-bin %s'
        #    search = takeComand().lower()
        #    wb.get(firefoxpath).open_new_tab(search + '.com')
        
        elif 'stack overflow' in query:
            wb.open("www.stackoverflow.com")
        
        elif 'facebook' in query:
            wb.open("www.facebook.com")
            
        elif 'crunchyroll' in query:
            wb.open('www.crunchyroll.com')
        
        #Reviar para cambiar edge por chrome o firefox
        elif 'search in web' in query:
            speak("What should i search? ")
            search = takeComand().lower()
            wb.open(search + '.com')
        
        elif 'logout' in query:
            os.system("shutdown -l")
        
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        
        elif 'spotify' in query:
            spotify()
        
        elif 'remember that' in query:
            speak("What should I remember?")
            data = takeComand()
            speak("You said me to remember that" + data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()
        
        elif 'do you know anyting' in query:
            remember = open('data.txt','r')
            speak("you said me to remember that" + remember.read())
            
        #elif 'open app(in here name off app)'
            #nameapppath = '/lib/firefox-esr/firefox-bin %s'(Este es un ejemplo para abrir firefox)
            #os.startfile(nameapppath)
        
        #Esto es para  detectar actualizaciones una terminal    
        #elif 'update' in query:
        #    zshpath = '/usr/bin/zsh'
        #    os.system("gnome-terminal -e 'bash -c \"sudo apt-get update; exec bash\"'")
        #    #Cambiar gnome=terminal por zsh
        
        #Esto es para actualizar una terminal en linux   
        elif 'upgrade' in query:
            zshpath = '/usr/bin/zsh'
            os.system("gnome-terminal -e 'bash -c \"sudo apt-get upgrade; exec bash\"'")
            #Cambiar gnome=terminal por zsh
        
        #Esto es para abrir una terminal en linux
        elif 'terminal' in query:
            zshpath = '/usr/bin/zsh'
            os.system("gnome-terminal -e 'bash -c \"exec bash\"'")
            #Cambiar gnome=terminal por zsh
        
        elif 'screenshot' in query:
            screenshot()
            speak("done!!")
        
        #elif 'camera' in query:
        #    cap = cv2.VideoCapture(0)
        #    while True:
        #        ret, img = cap.read()
        #        cv2.imshow('webcam',img)
        #        k = cv2.waitKey(50)
        #        if k == 27:
        #            break;
        #    cap.release()
        #    cv2.destroyAllWindows()
        
        #Solo linux 
        elif 'alsamixer' in query:
            os.system('alsamixer')
           
        elif 'cpu' in query:
            cpu()
            
        elif 'joke' in query:
            speak("Redy sir?")
            jokes()
        
        elif 'send message' in query:
            message()
            
        elif 'youtube song' in query:
            song()
        
        elif 'offline' in query:
            speak("Good bye sir!")
            quit()

takeComand()
#Aprender electronica y circuitos para crear sistema de automatizacion con jarvis