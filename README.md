# 🗣️ Voice Typing Document Assistant

A hands-free **Text-to-Speech** Python application designed for **typing documents using voice commands**. This tool allows you to create structured documents with **titles**, **subtitles**, **content**, **punctuation**, and **formatting** — all by speaking naturally.

---

## ✨ Features

- 🎤 **Continuous Voice-to-Text**: Speak continuously to type into any document field using your microphone.
- 📝 **Voice-Driven Structure**:
  - Say **"title"** followed by your heading to insert a bold, large title.
  - Say **"subtitle"** followed by text to insert a smaller subheading.
  - Regular speech is typed as body content.
- 🔠 **Text Formatting by Voice**:
  - **"comma"** → inserts `,`
  - **"period"** → inserts `.`
  - **"new line"** → creates a new line
  - **"backspace"** → deletes the last word
  - **"title bold"** → creates a bold, larger title
- 🖱️ **Auto-Typing with PyAutoGUI**: Automatically types the recognized text into the currently focused text area or document field.
- 🔠 **Auto-Capitalization**: Automatically capitalizes titles, subtitles, and the first word of sentences.

---

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Tech-master1234/TTS.git
cd TTS
```
## 2. Install Required Dependencies

```bash
pip install -r requirements.txt
```

- Make sure you have:

- Python 3.7+

- A working microphone

- Internet connection (for speech recognition)

- Here's your provided content fully converted into proper **Markdown (`.md`)** format, including all titles, code blocks, and structured tables:

---


## ▶️ Usage

### Run the App:
```bash
python main.py
```

### Start Speaking:
```text
"title Bold The Future of AI"

"subtitle AI in Everyday Life"

"Artificial intelligence is changing the world period new line It helps automate tasks comma enhance decision making comma and more period"
```

**Stop Listening**: Say `"stop"` to end the session.

---

## 🧠 Voice Command Reference

| Voice Command | Action                              |
|---------------|--------------------------------------|
| `title`       | Insert title (bold, large)           |
| `subtitle`    | Insert subtitle (smaller than title) |
| `comma`       | Inserts `,`                          |
| `period`      | Inserts `.`                          |
| `new line`    | Adds a new line                      |
| `backspace`   | Deletes last word                    |
| `stop`        | Stops the session                    |

---

## 📂 Project Structure

```bash
voice-typing-docs/
│
├── voice_typing.py          # Main application script
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
└── assets/                  # Optional assets (icons, UI, etc.)
```

---

## 💡 Future Improvements

- GUI version with a live preview  
- Export as `.docx` or `.pdf`  
- Custom keyword configuration  
- Multi-language support
```

---

