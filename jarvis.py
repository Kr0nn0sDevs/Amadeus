import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[56].id)

engine.say("Welcome Christian")
engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak(day)
    speak(month)
    speak(year)
    
def wishme():
    speak("Welcome back Christian")
    speak("The current time is")
    time()
    speak("The current date is")
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good Morning Christian")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Christian")
    elif hour >= 18 and hour < 24:
        speak("Good Evening Christian")
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

takeComand()
