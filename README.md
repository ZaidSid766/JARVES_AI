
# Jarvis Assistant - Personal AI Assistant

This repository contains a Python-based personal voice assistant named "Jarvis." It is capable of recognizing voice commands, executing tasks, and responding to queries with speech output. Jarvis is designed to assist with common tasks like searching the web, opening applications, retrieving the time, and playing YouTube videos, among other features. Additionally, it provides a graphical user interface (GUI) built with Tkinter for manual command input.


## Features

- Voice Recognition: The assistant listens to voice commands using the speech_recognition library.

- Speech Output: Jarvis responds through text-to-speech functionality, powered by pyttsx3.

- Task Execution: The assistant can open web browsers, applications, play media, fetch news, and more.

- Manual Input: In addition to voice commands, users can manually input text commands through the GUI.

- GUI: A Tkinter-based interface provides buttons to control listening modes and a text box for manual input.

- Hotkeys: Keyboard shortcuts are available to start or pause the listening mode.

- Automated Greetings: The assistant greets the user based on the time of day.


## Libraries and Modules Used
## Python Libraries

- tkinter: Used for building the graphical user interface (GUI).

- pyttsx3: Text-to-speech library for responding to the user.

- speech_recognition: For recognizing and processing voice commands.

- os: Allows the assistant to open applications and files on the system.

- webbrowser: Automates opening websites in the browser.

- datetime: Used for time-based functionalities like greeting the user and reporting the current time.

- decouple: To securely manage environment variables, like the username and assistant's name, through .env files.

- random: Used to select random responses in specific situations.

- keyboard: Detects keypress events to trigger functions.
## External Files
- conv.py: Contains random text responses used by the assistant in certain situations.

- online.py: Implements functionalities like web searches on Google, Wikipedia, fetching news, or playing videos on YouTube.

## Installation
- Python 3.x: Ensure that Python is installed.

- Pip: The package manager to install dependencies.

- Virtual Environment (Optional): It's recommended to create a virtual environment to isolate the project.
## Clone the Repository

```bash
 git clone https://github.com/yourusername/Jarvis-Assistant.git
cd Jarvis-Assistant
```
## Install Dependencies
```bash
pip install -r requirements.txt
```
## Set Up .env File
Create a .env file in the root directory with the following content:
```bash
USER="Your Name"
BOT="Jarvis"
```
This sets up your assistant's name and user name for personalized interactions.

## Running the Application
```bash
python main.py
```


## How It Works
## Voice Commands
Once the assistant is running, press Ctrl + Alt + Z to start voice recognition and Ctrl + Alt + X to pause it. The assistant listens for commands and processes them using Google’s speech recognition engine. It can handle a variety of tasks such as:

- Opening websites: e.g., “Open YouTube,” “Search on Google.”

- Executing system commands: e.g., “Open Notepad,” “Open Command Prompt.”

- Fetching the time: e.g., “What is the time?”

- Playing YouTube videos: e.g., “Play video on YouTube.”
## Manual input
If voice recognition is not preferred, users can type their commands into the text box at the bottom of the GUI and click “Send.” The assistant will process and respond to these commands in the same way it does for voice inputs.
## GUI Layout
The GUI is built using Tkinter and features:

- A title label for the assistant's name.

## Three buttons for:
1. Starting the voice recognition.
2. Pausing the voice recognition.
3. Running the assistant to process voice commands.
- A text box for manually typing commands.
- A "Send" button to submit text commands.

## Hotkeys
- Ctrl + Alt + Z : Start listening.

- Ctrl + Alt + X : Stop listening.
## Example Commands
- "Open YouTube": Opens the YouTube website in your browser.
- "What is the time?": Responds with the current time.
- "Search on Google": Prompts you for a search query, then searches on Google.
- "Search on Wikipedia": Prompts you for a topic, fetches a summary from Wikipedia, and opens the article.
## Future Enhancements
- Add more commands for opening specific files or directories.
- Integrate more APIs (e.g., weather information, stock prices).
- Enhance the GUI with more interactive elements and styling.
- Improve voice recognition accuracy by adding offline recognition support.
## Contributing
Feel free to open issues and submit pull requests. Contributions are welcome, whether it's bug fixes, feature requests, or optimizations.
