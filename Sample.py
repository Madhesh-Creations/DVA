import calendar
import subprocess
import cv2
import playsound
import pyautogui
import pywhatkit
import wolframalpha
import pyttsx3
from word2number import w2n
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import smtplib
import ctypes
import time
import requests
import shutil

from Demos.getfilever import n
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

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


def recognize_numbers():
    # ask the user for the first number
    speak("Please say the first number.")
    print("Speak now:")
    first_number = takeCommand().replace(' ', '')
    print(f"You said: {first_number}")
    speak(f"You said: {first_number}")

    speak("Please say the second number.")
    print("Speak now:")
    second_number = takeCommand().replace(' ', '')
    print(f"You said: {second_number}")
    speak(f"You said: {second_number}")

    return first_number, second_number


# define a function to recognize user speech and extract mathematical operations
def recognize_operation():
    speak("Please say the mathematical operation you want me to perform.")
    print("Speak now:")
    operation = takeCommand().lower()
    if operation not in ['addition', 'subtraction', 'multiplication', 'division']:
        print("Invalid operation.")
        operation = None

    print(operation)

    return operation


# define a function to perform the calculation and speak the result
def perform_calculation(first_number, second_number, operation):
    first_number = int(first_number)
    second_number = int(second_number)

    res = 0

    if operation == 'addition':
        res = first_number + second_number
    elif operation == 'subtraction':
        res = first_number - second_number
    elif operation == 'multiplication':
        res = first_number * second_number
    elif operation == 'division' \
                      '':
        res = first_number / second_number

    return res


if __name__ == '__main__':
    clear = lambda: os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    username()

    while True:

        query = takeCommand().lower()
        command = query.split(" ")

        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command
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

        elif 'game' in command:
            speak("Welcome to the Mind Trick game! I will ask you three questions")
            # Define list of questions and answers
            questions = ["What starts with “e” and ends with “e” but only has one letter in it",
                         "Where is an ocean with no water?",
                         "What two things can you never eat for breakfast?"]
            answers = ["envelope", "map", "lunch and dinner"]

            n = 0

            # Ask each question and check answer
            for question in questions:
                speak(question)
                print(question)
                answer = takeCommand()
                if answer.lower() == answers[questions.index(question)]:
                    speak("Correct!")
                    n = n + 1
                else:
                    speak("Incorrect.")

            # End of game
            print("Your Score is", n)
            speak("Thanks for playing!")

        elif 'stack overflow' in command:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")

        elif "ip" in command:
            ip = requests.get('https://api.ipify.org').text
            print(ip)
            speak(f"Your ip address is {ip}")

        elif 'movie' in command:
            speak("enjoy your movie sir")
            movie_dir = "F:\\Movies\\Hollywood Movies\\Harry Potter"
            movies = os.listdir(movie_dir)
            print(movies)
            os.startfile(os.path.join(movie_dir, movies[1]))

        elif 'music' in command or "song" in command:
            speak("which song do you want")
            sa=takeCommand().lower()
            sa=sa.split(" ")
            # music_dir = "G:\\Song"
            if 'english' in sa:
                music_dir = "F:\\Music\\English Songs"
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[1]))
            elif 'tamil' in sa:
                music_dir = "F:\\Music\\Tamil Songs"
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[1]))
            elif 'anime' in sa:
                music_dir = "F:\\Music\\Anime Songs"
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[1]))

        elif 'time' in command:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"Sir, the time is {strTime}")
        elif 'date' in command:
            strDay = datetime.date.today().strftime("%B %d, %Y")
            speak(f"Today is {strDay}")
        elif 'day' in command:
            speak(f"Today is {datetime.datetime.now().strftime('%A')}")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            uname = query

        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            myname = takeCommand()
            speak("Thanks for naming me")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(myname)
            print("My friends call me", myname)

        elif 'exit' in query or "bye" in command or "you can leave" in query:
            speak("Thanks for giving me your time")
            exit()

        elif "who made you" in query or "who created you" in query:
            speak("I have been created Group of Kalki that Under the Guidance of Mr.T.MUTHAMILSELVAM")

        elif 'joke' in command:
            speak(pyjokes.get_joke())

        elif 'gmail' in command:
            webbrowser.open_new_tab("mail.google.com")
            speak("Google Mail open now")

        elif 'corona' in command:
            news = webbrowser.open_new_tab("https://www.worldometers.info/coronavirus/")
            speak('Here are the latest covid-19 numbers')

        elif "calculate" in command or "calculator" in command:
            speak("opening calculator")
            # recognize the user's speech input and extract numerical values and mathematical operation
            first_number, second_number = recognize_numbers()
            operation = recognize_operation()

            # perform the calculation and speak the result
            r = perform_calculation(first_number, second_number, operation)
            print(f"The {operation} of {first_number} and {second_number} is {r}.")
            speak(f"The {operation} of {first_number} and {second_number} is {r}.")

        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif 'open youtube and play' in query or 'on youtube' in query:
            if 'on youtube' in query:
                speak("Opening youtube")
                pywhatkit.playonyt(query.replace('on youtube', ''))
            else:
                speak("Opening youtube")
                pywhatkit.playonyt(query.replace('open youtube and play ', ''))

        elif 'play some songs on youtube' in query or 'play songs on youtube' in query:
            speak("Opening youtube")
            pywhatkit.playonyt('play random songs')

        elif 'typing' in query:
            speak("Opening typeracer")
            webbrowser.get(chrome_path).open("https://play.typeracer.com/")

        elif 'open google and search' in query or 'google and search' in query:
            url = 'https://google.com/search?q=' + query[query.find('for') + 4:]
            webbrowser.get(chrome_path).open(url)

        elif "who i am" in query:
            speak("If you talk then definitely your human.")

        elif 'power point' in command:
            speak("opening Power Point presentation")
            power = r"C:\\Users\\GAURAV\\Desktop\\Minor Project\\Presentation\\Voice Assistant.pptx"
            os.startfile(power)

        elif "who are you" in query:
            speak("I am your Desktop Assistant name Sophia")

        elif 'reason for you' in query:
            speak("I was created for college Final year Project by Group of Kalki ")

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "F:\\Wallpaper\\Your Name\\New folder",
                                                       0)
            speak("Background changed successfully")

        elif 'news' in command:
            speak("Showing top 5 news of today.")
            print("-----------------------------Top 5 news of all categories.----------------------------")
            r = requests.get('http://newsapi.org/v2/top-headlines?country=in&apiKey=329416dc10ea4588a0a8f6b233116393')
            data = json.loads(r.content)
            for i in range(5):
                print(f'News {i + 1}:  ')
                print(data['articles'][i]['title'] + '\n')
                speak(data['articles'][i]['title'] + '\n')

        elif 'lock window' in command:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in command:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'recycle bin' in command:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif 'find location of' in query or 'show location of' in query or 'find location for' in query or 'show location for' in query:
            if 'of' in query:
                url = 'https://google.nl/maps/place/' + query[query.find('of') + 3:] + '/&amp'
                webbrowser.get(chrome_path).open(url)
            elif 'for' in query:
                url = 'https://google.nl/maps/place/' + query[query.find('for') + 4:] + '/&amp'
                webbrowser.get(chrome_path).open(url)

        elif "what is my exact location" in query or "What is my location" in query or "my current location" in query or 'exact current location' in query:
            url = "https://www.google.com/maps/search/Where+am+I+?/"
            webbrowser.get().open(url)
            speak("Showing your current location on google maps...")

        elif "where am i" in query:
            Ip_info = requests.get('https://api.ipdata.co?api-key=test').json()
            loc = Ip_info['Trichy']
            speak(f"You must be somewhere in {loc}")

        elif 'send some files through bluetooth' in query or 'send file' in command or 'share' in command or 'open bluetooth' in query:
            speak("Opening bluetooth...")
            os.startfile(r"C:\Windows\System32\fsquirt.exe")

        elif "take a photo" in query or "photo" in command or "take selfie" in query or "selfie" in command:
            videoCaptureObject = cv2.VideoCapture(0)
            result = True
            a = os.getcwd()
            if not os.path.exists("../Camera"):
                os.mkdir("../Camera")
            os.chdir(a + '\Camera')
            ImageName = "Image-" + str(datetime.datetime.now()).replace(':', '-') + ".jpg"
            while result:
                ret, frame = videoCaptureObject.read()
                cv2.imwrite(ImageName, frame)
                result = False
            videoCaptureObject.release()
            cv2.destroyAllWindows()
            os.chdir(a)
            playsound.playsound("../camera-shutter-click.mp3")
            Location = "Camera\\" + ImageName
            os.startfile(Location)
            speak("Captured picture is stored in Camera folder.")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "whatsapp" in command or "send a whatsapp message" in query:
            speak("Please tell me the mobile number whom do you want to send message.")
            mobile_number = None
            while True:
                mobile_number = takeCommand().replace(' ', '')
                if mobile_number[0] == '0':
                    mobile_number = mobile_number[1:]
                if not mobile_number.isdigit() or len(mobile_number) != 10:
                    speak("Please say it again")
                else:
                    break
            mobile_number.replace(' ', '')
            speak("Tell me your message......")
            message = takeCommand()
            speak("Opening whatsapp web to send your message.")
            speak("Please be patient, sometimes it takes time.\nOR In some cases it does not works.")
            while True:
                try:
                    pywhatkit.sendwhatmsg("+91" + mobile_number, message, datetime.datetime.now().hour,
                                          datetime.datetime.now().minute + 1)
                    break
                except Exception:
                    pass
            time.sleep(20)
            speak('Message sent successfully.')

        elif "weather" in command or "temperature" in command:
            base_url = "http://api.openweathermap.org/data/2.5/weather?q=Trichy,IN&units=metric&appid=ea45752424c9cad83b4f5c836ced6b1a"
            data = requests.get(base_url).json()
            speak("-----------------------------Weather Report of Trichy City------------------------------")
            print("Temperature:   " + str(int(data['main']['temp'])) + ' Celsius\n' +
                  "Wind Speed:    " + str(data['wind']['speed']) + ' m/s\n' +
                  "Latitude:      " + str(data['coord']['lat']) +
                  "\nLongitude:     " + str(data['coord']['lon']) +
                  "\nDescription:   " + str(data['weather'][0]['description']) + '\n')

        elif "screenshot" in command:
            speak("Taking screenshot")
            img_captured = pyautogui.screenshot()
            a = os.getcwd()
            if not os.path.exists("../Screenshots"):
                os.mkdir("../Screenshots")
            os.chdir(a + '\Screenshots')
            ImageName = 'screenshot-' + str(datetime.datetime.now()).replace(':', '-') + '.png'
            img_captured.save(ImageName)
            os.startfile(ImageName)
            os.chdir(a)
            speak('Captured screenshot is saved in Screenshots folder.')

        elif "note" in command:
            # makig note
            speak("What would you like to write down?")
            data = takeCommand()
            date = datetime.datetime.now()
            filename = str(date).replace(':', '-') + '-note.txt'
            a = os.getcwd()
            if not os.path.exists('../Notes'):
                os.mkdir('../Notes')
            os.chdir(a + r'\Notes')
            with open(filename, 'w') as f:
                f.write(data)
            subprocess.Popen(['notepad.exe', filename])
            os.chdir(a)
            speak("I have a made a note of that.")

        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif 'open notepad' in command or 'open notepad' in query:
            speak('Opening notepad')
            os.startfile(r'C:\Windows\notepad.exe')

        elif 'open mspaint' in query or 'open microsoft paint' in query or 'microsoft paint' in command or 'mspaint' in command:
            speak("Opening Microsoft paint....")
            os.startfile('C:\Windows\System32\mspaint.exe')

        elif 'show me performance of my system' in query or 'open performance' in query or 'performance' in command or 'performance of my laptop' in command:
            speak("Opening Performance window....")
            os.startfile("C:\Windows\System32\perfmon.exe")

        elif 'open snipping tool' in query or 'snipping tool' in command:
            speak("Opening snipping tool....")
            os.startfile("C:\Windows\System32\SnippingTool.exe")

        # elif 'open code','open visual studio ','open vs code'],query):
        # SR.speak("Opeining vs code")
        # codepath=r"C:\Users\Vishal\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        # os.startfile(codepath)

        elif 'open file manager' in query or 'file manager' in command or 'open file explorer' in query or 'file explorer' in command:
            speak("Opening File Explorer")
            os.startfile("C:\Windows\explorer.exe")

        elif 'powershell' in command:
            speak("Opening powershell")
            os.startfile(r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe')

        elif 'command prompt' in command:
            speak("Opening command prompt")
            os.startfile(r'C:\Windows\System32\cmd.exe')

        elif 'open control panel' in query or 'control panel' in command:
            speak("Opening settings...")
            os.startfile('C:\Windows\System32\control.exe')

        elif 'vlc' in command:
            speak("Opening VLC media player")
            os.startfile(r"C:\Program Files\VideoLAN\VLC\vlc.exe")

        elif 'calendar' in command or 'display calendar' in query:
            print(calendar.calendar(2021))

        # NPPR9-FWDCX-D2C8J-H872K-2YT43
        elif "Sophia" in query:
            wishMe()
            speak("Sophia in your service Mister")
            speak(uname)

        elif "wikipedia" in command:
            webbrowser.open("wikipedia.com")

        elif "Good Morning" in query:
            speak("A warm" + query)
            speak("How are you Mister")
            speak(uname)

        elif "what is" in query or "who is" in query:

            # Use the same API key
            # that we have generated earlier
            client = wolframalpha.Client("7K75TE-2P35Y5PAL3")
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")

    # elif "" in query:
    # Command go here
    # For adding more commands
