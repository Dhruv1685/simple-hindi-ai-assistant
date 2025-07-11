import speech_recognition as sr

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening for Hindi command...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio, language='hi-IN')
        print("🗣️ Heard:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("🤖 Could not understand audio.")
        return ""
    except sr.RequestError:
        print("🤖 Speech recognition service unavailable.")
        return ""
