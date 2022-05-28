import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecogmition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui #pip install pyautogui
import psutil #pip install psutil
import pyjokes #pip install pyjokes
import pywhatkit as kit

#Revisar luego lo de spotify
# import openspotify

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[56].id)

#engine.say("Welcome Christian")
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
        speak("Good Morning Christian")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Christian")
    elif hour >= 18 and hour < 24:
        speak("Good Evening Christian")
    else:
        speak("Good Night Christian")

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
        speak("Good Night Christian")
    speak("Jarvis at your service. Plaese tell me how can i help you?")
    
#wishme()

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
    contact = takeComand().lower()
    list = [
        mom == +529671269131,
        dad == +529671226202
    ]
    if contact in list:
        return contact

if __name__ == "__main__":
    wishme()
    while True:
        query = takeComand().lower()
        
        if 'time' in query:
            time()
        
        elif 'date' in query:
            date()
        
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
        
        elif 'youtube' in query:
            wb.open("www.youtube.com")
            
        elif 'facebook' in query:
            wb.open("www.facebook.com")
        
        elif 'search in firefox' in query:
            speak("What should i search? ")
            #firefoxpath = '/lib/firefox-esr/firefox-bin %s'
            search = takeComand().lower()
            wb.open(f"{search}")
        
        
        elif 'logout' in query:
            os.system("shutdown -l")
        
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        
        #elif 'play spotify' in query:
        #    spotify()
        
        elif 'remember that' in query:
            speak("What should I remember?")
            data = takeComand()
            speak("You said me to remember that" + data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()
        
        elif 'do you know anything' in query:
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
        
        #Esto es para actualizar una terminal    
        elif 'upgrade' in query:
            zshpath = '/usr/bin/zsh'
            os.system("gnome-terminal -e 'bash -c \"sudo apt-get upgrade; exec bash\"'")
            #Cambiar gnome=terminal por zsh
        
        #Esto es para abrir una terminal    
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
         
        elif 'alsamixer' in query:
            os.system('alsamixer')
           
        elif 'cpu' in query:
            cpu()
            
        elif 'joke' in query:
            speak("Redy sir?")
            jokes()
        
        elif 'send message' in query:
            message()
        
        #Aprender electronica y circuitos para crear sistema de automatizacion con jarvis
        
        elif 'offline' in query:
            speak("Good bye sir!")
            quit()

takeComand()
