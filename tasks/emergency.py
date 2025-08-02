import pyttsx3

def trigger_emergency():
    speak("Emergency alert triggered! Calling emergency contact...")
    print("Emergency Contact Triggered!")

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()