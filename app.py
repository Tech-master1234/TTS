from flask import Flask, render_template, jsonify
import speech_recognition as sr
import pyautogui
import time
import sys
import threading
import queue

app = Flask(__name__, template_folder='templates')
command_queue = queue.Queue()
is_running = False

def get_audio(prompt="Speak:"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print(prompt)
            try:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio).lower().strip()
                if "terminate" in text:
                    print("Program terminated by command.")
                    return "terminate"
                return text
            except (sr.UnknownValueError, sr.RequestError):
                continue

def format_text(text, bold=True, enlarge_steps=0):
    if bold:
        pyautogui.hotkey('ctrl', 'b')
    for _ in range(enlarge_steps):
        pyautogui.hotkey('ctrl', 'shift', '>')
    pyautogui.write(text, interval=0.05)
    for _ in range(enlarge_steps):
        pyautogui.hotkey('ctrl', 'shift', '<')
    if bold:
        pyautogui.hotkey('ctrl', 'b')

def handle_title():
    title = get_audio("Speak the title:")
    if title != "skip":
        format_text(f"{title.upper()}\n", bold=True, enlarge_steps=4)

def handle_subtitle():
    subtitle = get_audio("Speak the subtitle:")
    if subtitle != "skip":
        format_text(f"{subtitle.capitalize()}\n", bold=True, enlarge_steps=2)
        pyautogui.press('tab')

def handle_content():
    print("Content mode: Say 'next line', 'full stop', 'delete', 'redo', 'undo', or 'end content' to exit.")
    first = True
    while True:
        text = get_audio("Speak content:")
        
        if text == "end content":
            print("Exiting content mode.")
            break
        elif text == "next line":
            pyautogui.typewrite(".")
            pyautogui.write("\n", interval=0.05)
            pyautogui.press("tab")
            first = True
        elif text == "full stop":
            pyautogui.typewrite(".")
            first = True
        elif text == "delete":
            pyautogui.hotkey('ctrl', 'backspace')
            first = True
        elif text == "redo":
            pyautogui.hotkey('ctrl', 'y')
            first = True
        elif text == "undo":
            pyautogui.hotkey('ctrl', 'z')
        else:
            if first:
                pyautogui.write(text.capitalize(), interval=0.05)
                first = False
            else:
                pyautogui.write(f", {text}", interval=0.05)

def voice_control_thread():
    global is_running
    while is_running:
        command = get_audio("Listening for command:")
        if command == "terminate":
            is_running = False
            break
        elif "title" in command:
            handle_title()
        elif "subtitle" in command:
            handle_subtitle()
        elif "content" in command:
            handle_content()
        else:
            print(f"Ignoring unrecognized command: {command}")

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/start")
def start_service():
    global is_running
    if not is_running:
        is_running = True
        threading.Thread(target=voice_control_thread).start()
        return jsonify({"status": "success", "message": "Voice service started."})
    return jsonify({"status": "info", "message": "Service already running."})

@app.route("/stop")
def stop_service():
    global is_running
    if is_running:
        is_running = False
        return jsonify({"status": "success", "message": "Voice service stopped."})
    return jsonify({"status": "info", "message": "Service not running."})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
