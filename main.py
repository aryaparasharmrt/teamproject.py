import smtplib as smt
import speech_recognition as sr
from email.message import EmailMessage
import pyttsx3 as p3  # converting test to voice
import pywhatkit as pw
import datetime
import wikipedia as wiki
# import pyaudio as py
import pyjokes as pj

dict = {'full stop': '.', 'exclamation mark': '!', 'star': '*', 's line': '$', 'at the rate': '@', 'hash': '#',
        'open parenthesis': '(', 'close parenthesis': ')', 'open braces': '{', 'close braces': '}',
        'open bracket': '[', 'close bracket': ']', 'caret': '^', 'percent': '%', 'plus': '+', 'minus': '-',
        'equal to': '=', 'comma': ',', 'invert': '"'}

listener = sr.Recognizer()
engine = p3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening..')
            listener.adjust_for_ambient_noise(source, duration=1)
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            # print(info)
            for i in dict:
                if i in info:
                    info = info.replace(i, dict[i])
                else:
                    pass
            print(info)
            return info

    except:
        pass


def send_email(receiver, subject, message):

    server = smt.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('aryaparasharj02@gmail.com', 'Arya123@#123')
    email = EmailMessage()
    email['From'] = 'aryaparasharj02@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'Aryan': 'aryaparasharj007@gmail.com',
    'Aayush': 'aayushgupta2708@gmail.com',
    'Arpit': 'arpit30699@gmail.com',
    'Deepanshu': 'deepanshuaggarwal1409@gmail.com',
    'Salik': 'salikshah1404@gmail.com',
    'Pallavi': 'pallavisharma80455@gamil.com'
}


def get_email_info():
    talk('To Whom you want to send the email')
    name = get_info()
    receiver = email_list[name]
    talk('What is the subject of your email')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)

def run_alexa():

    command = take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play', '')
        talk('playing'+ song)
        pw.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('Current time is'+ time)
    elif 'who' in command:
        person = command.replace('who','')
        info=wiki.summary(person,1)
        print(info)
        talk(info)
    elif 'joke' in command:
        print(pj.get_jokes())
        talk(pj.get_jokes())

while True:
    run_alexa()
get_email_info()
