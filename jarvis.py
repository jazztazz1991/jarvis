# This program was developed and written by Fluffy

# Libraries--------------------------------------------------------------
import pyttsx3
import speech_recognition as sr
import time

# Variables--------------------------------------------------------------
r = sr.Recognizer()
keywords = [("jarvis", 1), ("hey jarvis", 1), ]
source = sr.Microphone()
# Functions--------------------------------------------------------------
def Speak(text):
    rate = 100
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', rate+50)
    engine.say(text)
    engine.runAndWait()
def callback(recognizer, audio):
    try: 
        speech_as_text = recognizer.recognize_sphinx(audio, keyword_entries=keywords)
        print(speech_as_text)
        if "jarvis" in speech_as_text or "hey jarvis":
            Speak("Yes sir?")
            recognize_main()
    except sr.UnknownValueError:
        print("Oops! Didn't catch that")
def start_recognizer():
    print("Waiting for a keyword... Jarvis or Hey Jarvis")
    r.listen_in_background(source, callback)
    time.sleep(1000000)
def recognize_main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_sphinx(audio, language="en-US")
        data.lower()
        print("You said: " + data)
        # Greetings -----------------------------------------------------
        if "how are you" in data:
            Speak("I am Fine")
        elif "hello" in data:
            Speak("Hi there")
        else:
            Speak("I'm sorry sir, I did not understand your request")
    except sr.UnknownValueError:
        print("Jarvis did not understand your request")
    except sr.RequestError as e:
        print("Could not request results from Sphinx Recognition service; {0}".format(e))
# Main Program-----------------------------------------------------------
while 1:
    start_recognizer()
# Notes------------------------------------------------------------------
