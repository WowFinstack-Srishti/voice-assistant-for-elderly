import threading
import time

def set_reminder(seconds, message="Time to take medicine!"):
    def remind():
        time.sleep(seconds)
        print("Reminder:", message)
    threading.Thread(target=remind).start()