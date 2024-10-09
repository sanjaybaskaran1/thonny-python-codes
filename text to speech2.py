"""pyttsx3 python speech to text library used for speech recognition"""
import pyttsx3

"""initialise pyttsx3"""
engine = pyttsx3.init()

"""function for speak"""
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def getvoices(voice):
    voices = engine.getProperty('voices')
    if voice == 1:
        engine.setProperty('voice', voices[0].id)
    if voice == 2:
        engine.setProperty('voice', voices[1].id)
    speak("hello this is jarvis")


while True:
    voice = int(input("press 1 for male voice\npress 2 for female voice\n"))
    getvoices(voice=voice)
    text = input("Enter something: ")
    speak(text)