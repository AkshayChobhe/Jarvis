import os
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import random
import pyautogui

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    print("The current time is ", Time)

def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)
    print("The current date is " + str(day) + "/" + str(month) + "/" + str(year))

def wishme():
    print("Welcome back sir!!")
    speak("Welcome back sir!!")
    
    hour = datetime.datetime.now().hour
    if hour >= 4 and hour < 12:
        print("Good Morning Sir!!")
        speak("Good Morning Sir!!")
        
    elif hour >= 12 and hour < 16:
        print("Good Afternoon Sir!!")
        speak("Good Afternoon Sir!!")
        
    elif hour >= 16 and hour < 24:
        print("Good Evening Sir!!")
        speak("Good Evening Sir!!")
        
    else:
        print("Good Night Sir, See You Tommorrow.")
        speak("Good Night Sir, See You Tommorrow")

    print("Jarvis at your service sir, please tell me how may I help you.")
    speak("Jarvis at your service sir, please tell me how may I help you.")
    

def screenshot():
    img = pyautogui.screenshot()
    img.save("E:\\Jarvis\\Jarvis\\ss1.png")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening , Sir")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        speak("Recognizing")
        query = r.recognize_google(audio, language="en-in")
        print(query)

    except Exception as e:
        print(e)
        speak("Please say that again")
        return "Try Again"

    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "who are you" in query:
            print("I'm JARVIS created by Akshay and I'm a desktop voice assistant.")
            speak("I'm JARVIS , a desktop voice assistant , created by Akshay")
                      
        elif "how are you" in query:
            print("I'm fine sir, What about you?")
            speak("I'm fine sir, What about you?")

        elif "fine" in query:
            print("Glad to hear that sir!!")
            speak("Glad to hear that sir!!")
            
        elif "good" in query:
            print("Glad to hear that sir!!")
            speak("Glad to hear that sir!!")     

        elif "wikipedia" in query:
            try:
                speak("Ok wait sir, I'm searching...")
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except:
                speak("Can't find this page sir, please ask something else")
        
        elif "open youtube" in query:
            wb.open("youtube.com") 

        elif "open google" in query:
            wb.open("google.com") 
   
        elif "open stack overflow" in query:
            wb.open("stackoverflow.com")

        elif "play music" in query:
            song_dir = "E:\\Films\\Songs"
            songs = os.listdir(song_dir)
            print(songs)
            x = len(songs)
            y = random.randint(0,x)
            os.startfile(os.path.join(song_dir, songs[y]))

        elif "open chrome" in query:
            chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)

        elif "search on chrome" in query:
            try:
                speak("What should I search?")
                print("What should I search?")
                chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                search = takecommand()
                wb.get(chromePath).open_new_tab(search)
                print(search)

            except Exception as e:
                speak("Can't open now, please try again later.")
                print("Can't open now, please try again later.")
            
        
        elif "remember that" in query:
            speak("What should I remember")
            data = takecommand()
            speak("You said me to remember that" + data)
            print("You said me to remember that " + str(data))
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you remember anything" in query:
            remember = open("data.txt", "r")
            speak("You told me to remember that" + remember.read())
            print("You told me to remember that " + str(remember))

        elif "screenshot" in query:
            screenshot()
            speak("I've taken screenshot, please check it")

        elif ("bye" in query) or ("quit" in query) or ("offline" in query):
            speak("Have a good day , sir")
            quit()