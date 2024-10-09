import pyttsx3

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("hello this is jarvis")
speak("thanks for creating me")
speak("your so cool")


