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

def process_command(text):
    words = text.lower().split()
    for word in words:
        cmd = match_command(word, commands)
        if cmd:
            if cmd == 'time':
                current_time = datetime.now().strftime("%H:%M")
                speak(f"The current time is {current_time}.")
            elif cmd == 'reminder':
                speak("Setting a medicine reminder for 10 seconds.")
                set_reminder(10, "Time to take your medicine!")
            elif cmd == 'emergency':
                trigger_emergency()
            elif cmd == 'weather':
                speak(get_weather())
            elif cmd == 'exit':
                speak("Goodbye!")
                exit()
            return
    speak("Sorry, I didn't understand that command. Please try again.")

def run_assistant():
    speak("Hello! I am you voice assistant. Speak now.")
    while True:
        command = listen_command()
        if command:
            print("Heard:", command)
            process_command(command)
        #else:
        #    speak("I didn't catch that. Please try again.")

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