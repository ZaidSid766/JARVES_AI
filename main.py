import tkinter as tk
from tkinter import Canvas
import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import datetime
from decouple import config
from random import choice
import threading
import keyboard
import time

USER = config("USER")
HOSTNAME = config("BOT")

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def greet_me():
    hour = datetime.datetime.now().hour
    greetings = [
        f"Good morning {USER}, ready for another day?",
        f"Good afternoon {USER}, let's get to work!",
        f"Good evening {USER}, how can I assist you tonight?",
    ]
    if 6 <= hour < 12:
        greeting = greetings[0]
    elif 12 <= hour < 16:
        greeting = greetings[1]
    else:
        greeting = greetings[2]

    say(greeting)
    update_status("Idle", "Waiting for your command...")

listening = False
status_text = "Idle"

def start_listening():
    global listening
    listening = True
    update_status("Listening", "Listening for your command...")
    animate_waveform()
    animate_eye()

def pause_listening():
    global listening
    listening = False
    update_status("Idle", "Stopped listening.")
    print("Stopped listening")

keyboard.add_hotkey("ctrl+alt+z", start_listening)
keyboard.add_hotkey("ctrl+alt+x", pause_listening)

def take_command():
    update_status("Listening", "Listening for your command...")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        audio = r.listen(source, timeout=10)

    update_status("Processing", "Processing your command...")
    try:
        query = r.recognize_google(audio, language="en-in")
        update_status("Idle", f"Command recognized: {query}")
        return query
    except Exception as e:
        update_status("Error", f"Could not recognize command. Error: {e}")
        return None

def execute_command(query):
    if not query:
        return
    update_status("Executing", f"Executing command: {query}")
    sites = [
        ["youtube", "https://www.youtube.com/"],
        ["google", "https://www.google.co.in/"],
        ["facebook", "https://www.facebook.com/"],
        ["instagram", "https://www.instagram.com/"],
        ["wikipedia", "https://www.wikipedia.org/"]
    ]
    for site in sites:
        if f"open {site[0]}".lower() in query.lower():
            say(f"Opening {site[0]}...")
            webbrowser.open(site[1])
            return
    if "the time" in query.lower():
        strfTime = datetime.datetime.now().strftime("%H:%M:%S")
        say(f"The time is {strfTime}")
        return
    if "open camera" in query.lower():
        say("Opening camera...")
        os.system("start microsoft.windows.camera:")
        return
    if "hello jarvis" in query.lower():
        say("Hello! How can I help you?")
        return
    if "stop" in query.lower():
        pause_listening()
        say("Stopping as requested.")
        return
    if "open command prompt" in query.lower():
        say("Opening command prompt...")
        os.system('start cmd')
        return
    if "open notepad" in query.lower():
        say("Opening notepad...")
        os.system('"C:\\Windows\\notepad.exe"')
        return

    say("Sorry, I didn't recognize that. Please try again.")
    update_status("Idle", "Waiting for your next command...")

def run_assistant():
    if listening:
        query = take_command()
        if query:
            execute_command(query)

root = tk.Tk()
root.title("Jarvis Assistant")
root.geometry("1000x750")
root.configure(bg="#101010")

canvas = Canvas(root, width=1000, height=750, bg="#101010", highlightthickness=0)
canvas.pack()

outer_circle = canvas.create_oval(400, 300, 600, 500, outline="#00FFFF", width=3)
inner_circle = canvas.create_oval(420, 320, 580, 480, outline="#00FFFF", width=2)
core_circle = canvas.create_oval(450, 350, 550, 450, fill="#00FFFF", width=0)

wave_lines = []
for i in range(20):
    line = canvas.create_line(450 + i * 5, 600, 450 + i * 5, 580, fill="#00FFFF", width=2)
    wave_lines.append(line)

response_text = canvas.create_text(500, 550, text="How can I help you?", fill="#00FFFF", font=("Helvetica", 16, "bold"))

status_label = tk.Label(root, text="Status: Idle", bg="#101010", fg="#00FFFF", font=("Helvetica", 14, "bold"))
status_label.place(x=30, y=30)

def update_status(status, message):
    global status_text
    status_text = status
    status_label.config(text=f"Status: {status_text}")
    canvas.itemconfig(response_text, text=message)

bg_lines = []
for _ in range(10):
    x1, y1 = choice(range(1000)), choice(range(750))
    x2, y2 = x1 + choice(range(100, 300)), y1 + choice(range(-10, 10))
    bg_line = canvas.create_line(x1, y1, x2, y2, fill="#004444", width=1)
    bg_lines.append(bg_line)

def animate_background():
    for line in bg_lines:
        canvas.move(line, choice([-1, 1]), choice([-1, 1]))
    root.after(50, animate_background)

def animate_eye():
    for i in range(10):
        canvas.itemconfig(inner_circle, outline=f"#{choice('0123456789ABCDEF') * 6}")
        canvas.itemconfig(core_circle, fill=f"#{choice('0123456789ABCDEF') * 6}")
        root.update()
        time.sleep(0.1)
    canvas.itemconfig(inner_circle, outline="#00FFFF")
    canvas.itemconfig(core_circle, fill="#00FFFF")

def animate_waveform():
    for i in range(20):
        height = choice(range(10, 30))
        canvas.coords(wave_lines[i], 450 + i * 5, 600, 450 + i * 5, 600 - height)
        canvas.itemconfig(wave_lines[i], fill=f"#{choice('0123456789ABCDEF') * 6}")
    root.after(100, animate_waveform)

button_style = {
    "bg": "#00FFFF",
    "fg": "#101010",
    "font": ("Helvetica", 14, "bold"),
    "activeforeground": "#FFFFFF",
    "borderwidth": 0,
}

start_button = tk.Button(root, text="Start Listening", command=start_listening, **button_style)
start_button.place(relx=0.1, rely=0.87, relwidth=0.25, height=50)

stop_button = tk.Button(root, text="Stop Listening", command=pause_listening, **button_style)
stop_button.place(relx=0.4, rely=0.87, relwidth=0.25, height=50)

run_button = tk.Button(root, text="Run Assistant", command=run_assistant, bg="#FFD700", fg="#000000",
                       font=("Helvetica", 14, "bold"), activeforeground="#FFC107", borderwidth=0)
run_button.place(relx=0.7, rely=0.87, relwidth=0.25, height=50)

greet_me()
animate_background()
root.mainloop()
