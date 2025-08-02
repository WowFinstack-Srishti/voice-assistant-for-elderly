from voice_module import listen_command
from soundex_module import match_command
from gui import show_gui
from tasks.reminder import set_reminder
from tasks.emergency import trigger_emergency
from tasks.weather import get_weather
import pyttsx3
from datetime import datetime

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

commands = ["time", "reminder", "emergency", "weather", "exit"]

def main():
    while True:
        user_input = listen_command().lower()
        print("Heard:", user_input)

        for word in user_input.split():
            cmd = match_command(word, commands)
            if cmd == 'time':
                from datetime import datetime
                speak("Current time is " + datetime.now().strftime("%H:%M"))
            elif cmd == 'reminder':
                from tasks.reminder import set_reminder
                set_reminder(10)
                speak("Reminder set for 10 seconds.")
            elif cmd == 'emergency':
                speak("Calling emergency contact...")
            elif cmd == 'weather':
                speak("Weather feature is coming soon.")
            else:
                speak("Please say a valid command.")

if __name__ == "__main__":
    main()