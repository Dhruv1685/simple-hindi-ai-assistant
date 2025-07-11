from gtts import gTTS
import os
import uuid
from playsound import playsound

def speak(text):
    try:
        print("🗣️", text)
        tts = gTTS(text=text, lang='hi')
        filename = f"voice_{uuid.uuid4().hex}.mp3"

        # Save in same folder as this script
        base_path = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(base_path, filename)

        tts.save(full_path)
        playsound(full_path)
        os.remove(full_path)

    except Exception as e:
        print("❌ Speak error:", e)
