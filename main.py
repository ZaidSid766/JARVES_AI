import tkinter as tk
from tkinter import messagebox, Canvas, PhotoImage
import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import datetime
from decouple import config
from conv import random_text
from random import choice
from online import search_on_google, search_on_wikipedia,get_news,youtube
import keyboard

USER = config("USER")
HOSTNAME = config("BOT")
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def greet_me():
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        say(f"Good morning {USER},I am {HOSTNAME}, How may I assist you?")
    elif 12 <= hour < 16:
        say(f"Good afternoon {USER},I am {HOSTNAME}, How may I assist you?")
    elif 16 <= hour < 24:
        say(f"Good evening {USER},I am {HOSTNAME}, How may I assist you?")

listening = False
def start_listening():
    global listening
    listening = True
    print("Listening...")

def pause_listening():
    global listening
    listening = False
    print("Stopped listening")

keyboard.add_hotkey("ctrl+alt+z", start_listening)
keyboard.add_hotkey("ctrl+alt+x", pause_listening)

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        audio = r.listen(source, timeout=20)
        print("Recognizing...")
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            print(f"Error: {e}")
            return "Error"

def execute_command(query):
    sites = [
        ["youtube", "https://www.youtube.com/"],
        ["google", "https://www.google.co.in/"],
        ["facebook", "https://www.facebook.com/"],
        ["instagram", "https://www.instagram.com/"],
        ["wikipedia", "https://www.wikipedia.org/"]
    ]
    for site in sites:
        if f"open {site[0]}".lower() in query.lower():
            say(f"Opening {site[0]} sir...")
            webbrowser.open(site[1])
            return
        if "open my video".lower() in query.lower():
            video_path = "C:\\images\\MIET\\Dandiya NIght 2K23.mp4"
            os.startfile(video_path)
            return
        if "the time".lower() in query.lower():
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"The time is {strfTime}")
            return
        if "open camera".lower() in query.lower():
            say("Opening camera...")
            os.system("start microsoft.windows.camera:")
            return
        if "hello jarvis".lower() in query.lower():
            say("What can I do for you?")
            return
        if "stop".lower() in query.lower():
            pause_listening()
            say(choice(random_text))
            return
        if "open command prompt".lower() in query.lower():
            say("Opening command prompt...")
            os.system('start cmd')
            return
        if "open notepad".lower() in query.lower():
            say("Opening notepad...")
            os.system('"C:\\Windows\\notepad.exe"')
            return
        if "play video on youtube".lower() in query.lower():
            say("What do you want to watch on YouTube?")
            video = take_command().lower()
            webbrowser.open(f"https://www.youtube.com/results?search_query={video}")
            return
        if "search on google".lower() in query.lower():
            say(f"What do you want to search on Google, {USER}?")
            search_query = take_command().lower()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            return
        if "search on wikipedia".lower() in query.lower():
            say("What do you want to search on Wikipedia?")
            search = take_command().lower()
            results = search_on_wikipedia(search)
            say(f"According to wikipedia,{results}")
            say("I am opening wikipedia webpage for your command")
            webbrowser.open(f"https://en.wikipedia.org/wiki/{search}")
            #messagebox.showinfo("Wikipedia Search", "\n".join(results))
            return
        if "give me news".lower() in query.lower():
            say(f"i am reading the latest headline of today sir....")
            say(get_news())
            say("i am printing on screen sir....")
        messagebox.showinfo("News", "\n".join(get_news()))
        return

    say("Sorry, I didn't recognize that. Please try again.")

def run_assistant():
    if listening:
        query = take_command().lower()
        execute_command(query)

class SquareButton:
    def __init__(self, canvas, x, y, width, height, text, command):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.command = command
        self.text = text
        self.id = self.canvas.create_rectangle(x-width//2, y-height//2, x+width//2, y+height//2, fill="#FF5733", outline="#FF5733", activefill="#FF8C69")
        self.text_id = self.canvas.create_text(x, y, text=text, fill="white", font=("Helvetica", 16, "bold"))
        self.canvas.tag_bind(self.id, '<ButtonPress-1>', self.on_click)
        self.canvas.tag_bind(self.text_id, '<ButtonPress-1>', self.on_click)

    def on_click(self, event):
        self.command()

root = tk.Tk()
root.title("Jarvis Assistant")
root.geometry("600x800")
root.configure(bg="#1F1B24")

canvas = Canvas(root, width=600, height=800, bg="#1F1B24", highlightthickness=0)
canvas.pack()

label = tk.Label(root, text="Jarvis Assistant", font=("Helvetica", 28, "bold"), bg="#1F1B24", fg="#FFD700")
label.place(x=150, y=30)

# Create square buttons with new colors and styles
SquareButton(canvas, 300, 250, 200, 80, "Start Listening", start_listening)
SquareButton(canvas, 300, 380, 210, 80, "Pause Listening", pause_listening)
SquareButton(canvas, 300, 510, 200, 80, "Run Assistant", run_assistant)

# Add a text area for manual input
input_text = tk.Text(root, height=3, width=45, font=("Helvetica", 14), bg="#333", fg="white", insertbackground="white")
input_text.place(x=75, y=650)

def manual_command():
    query = input_text.get("1.0", tk.END).strip().lower()
    execute_command(query)
    input_text.delete("1.0", tk.END)

send_button = tk.Button(root, text="Send", command=manual_command, bg="#FFD700", fg="#1F1B24", font=("Helvetica", 14, "bold"), borderwidth=0)
send_button.place(x=510, y=710)

greet_me()

root.mainloop()