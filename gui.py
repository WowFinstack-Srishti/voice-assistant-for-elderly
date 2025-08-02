import tkinter as tk

def run_gui():
    window = tk.Tk()
    window.title("Voice-based assistant for Elderly Care")
    window.geometry("400x300")

    label = tk.Label(window, text="Welcome to the Voice-based Assistant for Elderly Care", font=("Arial", 14))
    label.pack(pady=20)

    status = tk.Label(window, text="Status: Ready", font=("Arial", 14))
    status.pack()

    window.mainloop()