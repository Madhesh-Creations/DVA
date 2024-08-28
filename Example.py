'''

# Packages

from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

from PIL import ImageTk

Window = Tk()

Window.geometry("300x300")
Window.title("Sophia Assistant")
Window.configure(bg='#add8e6')
# 2c4557


def startme():
    pass


def continueme():
    pass


image = Image.open("D:\PyCharm\EX\Final Year Project\start11.png")
resize_image = image.resize((66, 66))
img = ImageTk.PhotoImage(resize_image)


image1 = Image.open("D:\PyCharm\EX\Final Year Project\continue.png")
resize_image1 = image1.resize((66, 66))
img1 = ImageTk.PhotoImage(resize_image1)

btn = Button(Window, image=img, command=startme)

btn.pack(pady=10)

btn1 = Button(Window, image=img1, command=continueme)

btn1.pack(pady=100)




''
# Read the Image
image = Image.open("Image File Path")

# Resize the image using resize() method
resize_image = image.resize((width, height))

img = ImageTk.PhotoImage(resize_image)

# create label and add resize image
label1 = Label(image=img)
label1.image = img
label1.pack()


Window.mainloop()

'''

'''

import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Calculate the Square Root')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Type your Number:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)


def get_square_root():
    x1 = entry1.get()

    label3 = tk.Label(root, text='The Square Root of ' + x1 + ' is:', font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label3)

    label4 = tk.Label(root, text=float(x1) ** 0.5, font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 230, window=label4)


button1 = tk.Button(text='Get the Square Root', command=get_square_root, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()

'''

'''
# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

c = ""
# creates a Tk() object
master = Tk()



# sets the geometry of
# main root window
master.geometry("655x500")

label = Label(master, text="This is the main window")
label.pack(side=TOP, pady=10)

txt=Text(master)
txt.insert(master, c)
txt.pack()

# a button widget which will
# open a new window on button click
btn = Button(master,
             text="Hi")

# Following line will bind click event
# On any click left / right button
# of mouse a new window will be opened


btn.pack(pady=10)

# mainloop, runs infinitely
mainloop()



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            c="listening"
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
                c=command
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        c=info
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_alexa()

'''

import tkinter as tk
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

c = ""

root = tk.Tk()
T = tk.Text(root, height=10, width=30)
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
T.insert(tk.END, c)
tk.mainloop()

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            c = "Listening"
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
                c = command
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    c = command
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        c = info
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_alexa()

tk.mainloop()
