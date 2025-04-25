import speech_recognition as sr
import pyautogui
import time
import sys

def get_audio(prompt):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print(prompt)
            try:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio).lower().strip()
                if "stop" in text:
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
    while True:
        title = get_audio("Speak the title:")
        if title == "skip":
            break
        format_text(f"{title.upper()}\n", bold=True, enlarge_steps=4)
        break

def handle_subtitle():
    while True:
        subtitle = get_audio("Speak the subtitle:")
        if subtitle == "skip":
            pyautogui.hotkey('tab')
            break
        format_text(f"{subtitle.capitalize()}\n", bold=True, enlarge_steps=2)
        pyautogui.press('tab')
        break

def insert_subtitle_flow():
    pyautogui.write("\n", interval=0.05)
    handle_subtitle()

def insert_title_and_subtitle():
    pyautogui.write("\n", interval=0.05)
    handle_title()
    handle_subtitle()

def main():
    print("You have 5 seconds to focus your cursor in the text editor...")
    time.sleep(5)

    handle_title()
    handle_subtitle()

    print("Start speaking content. Say 'next line' to break line. Say 'stop the program' to exit.")
    first = True

    while True:
        text = get_audio("Speak:")

        if text == "next subtitle":
            insert_subtitle_flow()
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
        elif text == "title":
            insert_title_and_subtitle()
        else:
            if first:
                pyautogui.write(text.capitalize(), interval=0.05)
                first = False
            else:
                pyautogui.write(f", {text}", interval=0.05)

if __name__ == "__main__":
    main()
