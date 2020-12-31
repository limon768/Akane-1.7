import speech_recognition as sr
import time
import webbrowser as wb
from gtts import gTTS
import os
import playsound
import random
import urllib.request
import re

random_jokes = random.randint(1,2)
random_game_number= random.randint(1,10)
r = sr.Recognizer()


def audioStore(ask = False):
    if ask:
        Akane_talk(ask)
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)

        except sr.UnknownValueError:
            Akane_talk('Didnt get that')

        except sr.RequestError:
            Akane_talk('Request cant be done')

        return voice_data


def Akane_talk(audio_string):
    text_to_speech = gTTS(text=audio_string, lang='en')
    r = random.randint(1,100000000)
    file_name = 'file-' + str(r) + '.mp3'
    text_to_speech.save(file_name)
    playsound.playsound(file_name)
    print(audio_string)
    os.remove(file_name)
    

def response(voice_data):
    if "what is your name" in voice_data:
        name()
    if "tell me the time" in voice_data:
        Akane_talk(time.ctime())
    if "search" in voice_data:
        Akane_talk("working")
        crome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        search = audioStore("What do you want to search")
        url = 'https://google.com/search?q=' + search
        wb.get(crome_path).open(url)
        Akane_talk('Here is what i found ' + search)

    if "tell me a joke" in voice_data:
        Akane_talk("Here Goes one")
        #joke_name = "joke"+ random_jokes + ".txt"
        fh = open("joke1.txt",'r')
        myText = fh.read().replace("\n", " ")
        output = gTTS(text=myText, lang="en", slow= False)
        output.save("joke_name.mp3")
        playsound.playsound("joke_name.mp3")
        fh.close()
        os.remove()
          
    if "subreddit" in voice_data:
        Akane_talk("working")
        crome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        search = audioStore("What do you want to search")
        url = 'https://www.reddit.com/search/?q=' + search
        wb.get(crome_path).open(url)
        Akane_talk('Here is what i found ' + search)
    
    if "find location" in voice_data:
        Akane_talk("working")
        crome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        search = audioStore("What do you want to search")
        url = 'https://google.nl/maps/place/' + search + '/&amp;'
        wb.get(crome_path).open(url)
        Akane_talk('Location found ' + search)

    if "play music" in voice_data:
        crome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        Akane_talk("what song you want to listen")
        search = audioStore()
        new_search = search.replace(' ','+')
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + new_search)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        print(video_ids[0])
        url = "https://www.youtube.com/watch?v=" + video_ids[0]
        wb.get(crome_path).open(url)
    
    if "games" in voice_data:
        #Akane_talk("Ok, Guess a number between 1 to 10")
        AkanesNumber = random_game_number
        numberOfAkane = str(AkanesNumber)
        
        userNumber = audioStore("Ok, Guess a number between 1 to 10")
        intNumber = int(userNumber)

        if intNumber > AkanesNumber:
            Akane_talk("Your Number is too Big")
        elif intNumber<AkanesNumber:
            Akane_talk("Your Number is too Short")
        elif intNumber == AkanesNumber:
            Akane_talk("Good Game Well Played")

        Akane_talk("My number is " + numberOfAkane)

    if "help" in voice_data:
        Akane_talk("Here is the command list")
        Akane_talk("what is your name, tell me the time, search, tell me a joke, subreddit, find location, play music, games, exit") 

    if "exit" in voice_data:
        exit()


def name():
    Akane_talk("My Name is Akane")


time.sleep(1)

Akane_talk("Hi! My Name is Akane")
Akane_talk("How can i help you?")

while 1:
    voice_data = audioStore()
    response(voice_data)

