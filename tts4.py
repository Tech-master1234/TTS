import speech_recognition as sr
import pyautogui
import time
import platform

def process_text(text):
    replacements = {
        " comma": ",",
        " period": ".",
        " exclamation mark": "!",
        " question mark": "?",
        " new line": "\n",
        " newline": "\n"
    }

    for word, symbol in replacements.items():
        text = text.replace(word, symbol)
    return text

def press_bold_shortcut():
    system = platform.system()
    if system == "Darwin":  # macOS
        pyautogui.hotkey('command', 'b')
    else:  # Windows/Linux
        pyautogui.hotkey('ctrl', 'b')

def listen_and_type():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("🎤 Voice typing started. Say 'stop typing' to quit.")
    print("💬 Commands: 'title', 'title bold', 'comma', 'period', 'new line', etc.\n")
    print("⏳ Click into the document field you want to type into. Starting in 3 seconds...")
    time.sleep(3)

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)

        while True:
            print("Listening...")
            audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio).lower()
                print(f"You said: {text}")

                if "stop typing" in text:
                    print("🛑 Voice typing stopped.")
                    break

                elif text.startswith("title bold "):
                    title_text = text.replace("title bold ", "")
                    title_text = process_text(title_text)
                    press_bold_shortcut()
                    pyautogui.typewrite(title_text + "\n")
                    press_bold_shortcut()
                    print(f"📝 Bold title typed: {title_text}")

                elif text.startswith("title "):
                    title_text = text.replace("title ", "")
                    title_text = process_text(title_text)
                    pyautogui.typewrite(title_text + "\n")
                    print(f"📝 Title typed: {title_text}")

                else:
                    processed = process_text(text)
                    pyautogui.typewrite(processed + " ")

            except sr.UnknownValueError:
                print("❌ Could not understand. Try again.")
            except sr.RequestError as e:
                print(f"⚠️ Request error: {e}")

if __name__ == "__main__":
    listen_and_type()
