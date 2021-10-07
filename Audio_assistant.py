
import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3




def talk(words):
     print(words)
     #os.system('say' + words)
     engine = pyttsx3.init()
     engine.say(words)
     engine.runAndWait()
     
talk('Привет, ВДК45')


def command_ru():
     r = sr.Recognizer()

     with sr.Microphone() as source:
          print("Говорите!")
          r.pause_threshold = 1 # ждать команды
          audio = r.listen(source)
          r.adjust_for_ambient_noise(source, duration=1) 
     try:
          phrase_ru = r.recognize_google(audio, language='ru-RU').lower()
          #print('Вы сказали: ' +  phrase)
     except sr.UnknownValueError:
          #talk('try again!')
          phrase_ru = command_ru()
     return phrase_ru


def command():
     r = sr.Recognizer()

     with sr.Microphone() as source:
          print("Говорите!")
          r.pause_threshold = 1 # ждать команды
          audio = r.listen(source)
          r.adjust_for_ambient_noise(source, duration=1) 
     try:
          phrase = r.recognize_google(audio, language='en-US').lower()
          #print('Вы сказали: ' +  phrase)
     except sr.UnknownValueError:
          #talk('try again!')
          phrase = command()
     return phrase


def actions(phrase):
     if 'open twitch' in phrase:
          talk('Open twitch')
          url = 'https://www.twitch.tv/vdk45'
          webbrowser.open(url)

     if 'open youtube' in phrase:
          talk('Open youtube')
          url = 'https://www.youtube.com/'
          webbrowser.open(url)
     
     if 'stop' in  phrase:
          talk('ok')
          sys.exit()
     else:
          print('You said: ' +  phrase)


def actions_ru(phrase_ru):
     if 'открыть twitch' in phrase_ru:
          talk('Open twitch')
          url = 'https://www.twitch.tv/vdk45'
          webbrowser.open(url)

     if 'открыть youtube' in phrase_ru:
          talk('Open youtube')
          url = 'https://www.youtube.com/'
          webbrowser.open(url)

     if 'открыть гитхаб' in phrase_ru:
          talk('Open github')
          url = 'https://github.com/VDK45'
          webbrowser.open(url)
     
     if 'стоп' in  phrase_ru:
          talk('ok')
          sys.exit()
     else:
          print('Вы сказали: ' +  phrase_ru)


while True:
     actions_ru(command_ru())
     actions(command())
          







