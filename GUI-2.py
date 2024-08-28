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


def on_button_click():
    query = takeCommand().lower()
    command = query.split(" ")

    if 'from wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        speak("According to Wikipedia")
        output_text.insert(tk.END, results + "\n")
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


if __name__ == '__main__':
    clear = lambda: os.system('cls')

    clear()
    wishMe()
    username()

    root = tk.Tk()
    root.geometry("500x500")
    root.title("Voice Assistant")

    button = tk.Button(root, text="Start", command=on_button_click)
    button.pack()

    output_text = tk.Text(root, height=20, width=50)
    output_text.pack()

    root.mainloop()
