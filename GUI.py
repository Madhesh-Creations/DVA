'''
import tkinter as tk
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


root = tk.Tk()
T = tk.Text(root, height=40, width=40)
T.pack()
quote = """HAMLET: To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to. 'Tis a consummation
Devoutly to be wished."""
T.insert(tk.END, quote)
tk.mainloop()

'''


'''
import os
import tkinter as tk
import webbrowser
import requests
import speech_recognition as sr
import pyttsx3
import shutil
import pywhatkit
import datetime
import wikipedia
import pyjokes


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


myname = ""
uname = ""
MAX_LISTEN_TIME = 10
chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir !")

    elif 12 <= hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    myname = "Sophia"
    speak("I am your Assistant")
    speak(myname)


def username():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns
    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))
    speak("How can i Help you, Sir")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=MAX_LISTEN_TIME)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


if __name__ == '__main__':
    clear = lambda: os.system('cls')

    clear()
    wishMe()
    username()

    while True:

        query = takeCommand().lower()
        command = query.split(" ")

        if 'from wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "geeks" in command:
            speak("Opening GeeksforGeeks ")
            webbrowser.open("www.geeksforgeeks.com")

        elif 'youtube' in command:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'google' in command:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'stack overflow' in command:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")

'''
'''
from tkinter.ttk import *
import tkinter as tk
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


root = tk.Tk()
T = tk.Text(root, height=40, width=40)
T.pack()
quote = """HAMLET: To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to. 'Tis a consummation
Devoutly to be wished."""
T.insert(tk.END, quote)



btn=Button()
btn.pack()
tk.mainloop()

'''
'''
import os
import tkinter as tk
import webbrowser
import requests

import speech_recognition as sr
import pyttsx3
import shutil
import pywhatkit
import datetime
import wikipedia
import pyjokes

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Declaration of variables
myname = ""
uname = ""
MAX_LISTEN_TIME = 10
chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"


def speak(audio):
    """Speak the given text using the text-to-speech engine."""
    engine.say(audio)
    engine.runAndWait()

# Function to Wish


def wishMe():
    """Greet the user based on the current time."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir !")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir !")
    else:
        speak("Good Evening Sir !")

    myname = "Sophia"
    speak("I am your Assistant")
    speak(myname)

# Function to get username


def username():
    """Get the user's name and welcome them."""
    global uname

    speak("What should I call you, sir?")
    uname = takeCommand()
    speak(f"Welcome, Mister {uname}!")

    # Display a message in the GUI
    message_label.config(text=f"Welcome, Mister {uname}!")
    message_label.pack()

    speak("How can I help you, sir?")

# Function to take command


def takeCommand():
    """Listen for the user's voice command and return the text transcription."""
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=MAX_LISTEN_TIME)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to recognize your voice.")
        return "None"

    return query


def search_wikipedia():
    """Search for the user's query on Wikipedia and display the result."""
    query = wikipedia_entry.get().strip()
    speak('Searching Wikipedia...')
    results = wikipedia.summary(query, sentences=3)
    speak("According to Wikipedia")
    print(results)
    speak(results)

    # Display the result in the GUI
    results_text.config(state=tk.NORMAL)
    results_text.delete(1.0, tk.END)
    results_text.insert(tk.END, results)
    results_text.config(state=tk.DISABLED)


# Main
if __name__ == '__main__':
    clear = lambda: os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    username()

    # Create the GUI window
    window = tk.Tk()
    window.title("Voice Assistant")

    # Create the Wikipedia search interface
    wikipedia_frame = tk.Frame(window)
    wikipedia_frame.pack(side=tk.TOP, pady=10)

    wikipedia_label = tk.Label(wikipedia_frame, text="Search Wikipedia:")
    wikipedia_label.pack(side=tk.LEFT)

    wikipedia_entry = tk.Entry(wikipedia_frame, width=50)
    wikipedia_entry.pack(side=tk.LEFT)

    wikipedia_button = tk.Button(wikipedia_frame, text="Search

'''

'''
import os
import tkinter as tk
import webbrowser
import requests

import speech_recognition as sr
import pyttsx3
import shutil
import pywhatkit
import datetime
import wikipedia
import pyjokes


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Declaration of variables
myname = ""
uname = ""
MAX_LISTEN_TIME = 10
chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to Wish


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir !")

    elif 12 <= hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    myname = "Sophia"
    speak("I am your Assistant")
    speak(myname)

# Function to get username


def username():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))

    speak("How can i Help you, Sir")

# Function to take command


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=MAX_LISTEN_TIME)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


# Main
if __name__ == '__main__':
    clear = lambda: os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    username()

    # Create GUI
    root = tk.Tk()
    root.geometry("400x400")
    root.title("Virtual Assistant")

    # Define label and button widgets
    label = tk.Label(root, text="Press the button and speak")
    button = tk.Button(root, text="Speak")

    # Define button click event
    def button_click():
        query = takeCommand().lower()
        command = query.split(" ")

        # from wikipedia {query}
        if 'from wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # open GeeksforGeeks
        elif "geeks" in command:
            speak("Opening GeeksforGeeks ")
            webbrowser.open("www.geeksforgeeks.com")

        # open Youtube
        elif 'youtube' in command:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        # open Google
        elif 'google' in command:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

'''

import os
import tkinter as tk
import webbrowser
import requests
import speech_recognition as sr
import pyttsx3
import shutil
import pywhatkit
import datetime
import wikipedia
import pyjokes


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


myname = ""
uname = ""
MAX_LISTEN_TIME = 10
chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir !")

    elif 12 <= hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    myname = "Sophia"
    speak("I am your Assistant")
    speak(myname)


def username():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns
    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))
    speak("How can i Help you, Sir")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=MAX_LISTEN_TIME)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query

def start_assistant():
    clear = lambda: os.system('cls')

    clear()
    wishMe()
    username()

    while True:

        query = takeCommand().lower()
        command = query.split(" ")

        if 'from wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "geeks" in command:
            speak("Opening GeeksforGeeks ")
            webbrowser.open("www.geeksforgeeks.com")

        elif 'youtube' in command:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'google' in command:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'stack overflow' in command:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")

# GUI
root = tk.Tk()
root.geometry("300x100")
root.title("Virtual Assistant")

btn_start = tk.Button(root, text="Start Assistant", command=start_assistant)
btn_start.pack()

root.mainloop()
