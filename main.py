import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import sys
from datetime import date




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
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play' , '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'date' in command:
        today = date.today()
        print("current date:", today)
        d2 = current.strftime("%B %d, %Y")
        print("Today's Date is", d2)
        talk('The current date is ',d2)

    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif ' are you busy' in command:
        talk('yes , i am busy')

    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'open google' in command:
        talk(webbrowser.open_new('https://www.google.co.in/'))
    elif 'open instagram' in command:
        talk(webbrowser.open_new('https://www.instagram.com/'))
    elif 'stop' in command:
        talk('good bye, have a nice day !!')
        sys.exit()

    else:
        talk('Please say the command again.')


while True:
    run_alexa()