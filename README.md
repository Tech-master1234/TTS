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
git clone https://github.com/yourusername/voice-typing-docs.git
cd voice-typing-docs
