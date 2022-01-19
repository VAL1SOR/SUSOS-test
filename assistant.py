import speech_recognition as sr
import os
import time 
import pyttsx3
import pywhatkit as kt

def assistant():
    import pyttsx3

    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    tim = time.localtime()
    current_time = time.strftime("%H:%M:%S", tim)
    run = False
    start = True

    print("Close assistant?\n1. YES\n2. NO")
    res = str(input(">> "))

    if res == "1":
        os.system("python3 os.py")
    elif res == "2":
        pass
    while start:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language = "en-US")
                if text == "assistant":
                    engine.say("What do you want?")
                    engine.runAndWait()
                    start = False
                    run = True
            except:
                continue

    while run:

        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language = "en-US")
                print(text)
                if text == "open Google":
                    engine.say("Opening Google.")
                    engine.runAndWait()
                    os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
                    run = False
                    start = True
                elif text == "tell me more about you":
                    engine.say("I am a virtual assistant made by Satmari Radu Valentin in Python. isn't he a genius?")
                    engine.runAndWait()
                    run = False
                    start = True
                elif text == "what time is it" or text == "what time it is":
                    engine.say("Is: " + str(current_time))
                    engine.runAndWait()
                    run = False
                    start = True
                elif text == "close Google":
                    engine.say("Closing Google.")
                    engine.runAndWait()
                    os.system("TASKKILL /F /IM chrome.exe")
                    run = False
                    start = True
                else:
                    kt.search(str(text))
                    engine.say("Here are some results from the web.")
                    engine.runAndWait()
                    run = False
                    start = True
            except:
                engine.say("Sorry I could not recognize what you said")
                engine.runAndWait()
                run = False
                start = True