import tkinter as tk
import threading

def show_gui(callback):
    window = tk.Tk()
    window.title("Voice-based assistant for Elderly Care")
    window.geometry("400x200")

    label = tk.Label(window, text="Click to Speak", font=("Arial", 18))
    label.pack(pady=20)

    def on_click():
        threading.Thread(target=callback).start()

    btn = tk.Button(window, text="Start Listening", command=on_click, font=("Arial", 16), bg="lightblue")
    btn.pack(pady=10)

    window.mainloop()