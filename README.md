# 🤖 Hindi Voice Assistant using Gemini API

A voice-controlled Hindi assistant powered by Google's Gemini API. It listens to spoken Hindi commands, understands their meaning using AI, and runs relevant Python code — like opening applications, cleaning folders, searching the web, and more.

---

## ✨ Features

- 🎤 Understands and processes Hindi voice commands  
- 🧠 Uses Gemini (Google AI) for interpreting commands  
- 🖥️ Executes real Python actions (e.g., open apps, clean folders)  
- 🗂 Customizable command list via `command_list.txt`  
- 🔊 Hindi voice replies using `gTTS` and `playsound`  
- 💡 Simple, lightweight, and extendable

---

## 🗂️ Project Structure

```
project/
│
├── main.py                 # Main assistant logic
├── command_list.txt        # Hindi command-to-code mapping examples
├── .env                    # Contains Gemini API key
├── requirements.txt        # List of dependencies
└── README.md               # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/hindi-voice-assistant.git
cd hindi-voice-assistant
```

### 2. Install Required Packages

```bash
pip install -r requirements.txt
```

### 3. Configure Gemini API Key

Create a `.env` file in the project root with this content:

```env
GEMINI_API_KEY=your_google_gemini_api_key_here
```

🔑 You can get your Gemini API key from:  
[https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)

---

## 🧠 How It Works

1. **Voice Command Input**: User speaks in Hindi (e.g., "नोटपैड खोलो")  
2. **Command Lookup & Prompting**: Assistant sends the command + examples from `command_list.txt` to Gemini  
3. **AI Response**: Gemini returns an explanation and Python code  
4. **Code Extraction & Execution**: Assistant safely extracts and runs the code (after removing formatting)  
5. **Voice Feedback**: Assistant replies back in Hindi using `gTTS`

---

## 📜 Example Hindi Commands

The following sample commands are supported via `command_list.txt`:

| 🗣 Hindi Command                        | 🧠 Action (Python)                          |
|----------------------------------------|---------------------------------------------|
| "क्रोम खोलो"                          | `webbrowser.open("https://www.google.com")` |
| "नोटपैड खोलो"                        | `os.system("start notepad")`                |
| "रीसायकल बिन खोलो"                   | `os.system("start shell:RecycleBinFolder")` |
| "रीसायकल बिन के फाइल्स डिलीट करो"   | `winshell.recycle_bin().empty(...)`         |
| "डाउनलोड्स फोल्डर साफ करो"           | `shutil.rmtree("C:/Users/Dhruv/Downloads")` |
| "गूगल खोलो"                          | `webbrowser.open("https://www.google.com")` |
| "सिस्टम जानकारी दिखाओ"               | `os.system("systeminfo")`                   |
| "कंप्यूटर शटडाउन करो"                | `os.system("shutdown /s /t 5")`             |

You can add your own examples in `command_list.txt`.

---

## 📦 Dependencies

Your `requirements.txt` should include:

```
google-generativeai
python-dotenv
gTTS
playsound
speechrecognition
pyaudio
winshell
```

Install using:

```bash
pip install -r requirements.txt
```

If `pyaudio` fails, try:

```bash
pip install pipwin
pipwin install pyaudio
```

---

## 🔐 Safety Notes

- Python code from Gemini responses is sanitized by removing formatting like triple backticks or inline backticks before execution.
- Avoid commands that can harm your system (e.g., `os.remove`, `format`, etc.)
- Always validate or restrict code execution in production use cases.

---
