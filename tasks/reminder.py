import threading
import time
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def set_reminder(seconds, message):
    def remind():
        time.sleep(seconds)
        speak(message)
    threading.Thread(target=remind).start()