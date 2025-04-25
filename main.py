import speech_recognition as sr
import pyautogui
import time
import sys

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
                    sys.exit()
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

def main():
    print("You have 5 seconds to focus your cursor in the text editor...")
    time.sleep(5)

    print("Say 'title', 'subtitle', or 'content' to begin. Say 'stop' to exit.")
    
    while True:
        command = get_audio("Listening for command:")
        if "title" in command:
            handle_title()
        elif "subtitle" in command:
            handle_subtitle()
        elif "content" in command:
            handle_content()
        else:
            print(f"Ignoring unrecognized command: {command}")

if __name__ == "__main__":
    main()
