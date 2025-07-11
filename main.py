import tkinter as tk
import re
from listen import listen_command
from ai_brain import ask_gpt
from speak import speak
from execute import run_safe_code

def start_assistant():
    user_cmd = listen_command()
    if not user_cmd:
        speak("Main samajh nahi paaya.")
        return

    user_command.set(f"🗣️ Aapne kaha:\n{user_cmd}")
    speak("Soch raha hoon...")

    gpt_reply = ask_gpt(user_cmd)
    print("🔁 Gemini Response:\n", gpt_reply)
    gpt_response.set(f"🤖 Gemini ne kaha:\n{gpt_reply}")

    if "Action:" in gpt_reply and "Code:" in gpt_reply:
        try:
            # Extract action text
            action = gpt_reply.split("Action:")[1].split("Code:")[0].strip()

            # Extract code using regex to remove backticks or triple backticks
            code_match = re.search(r"Code:\s*`{0,3}(.*?)`{0,3}$", gpt_reply, re.DOTALL)
            code = code_match.group(1).strip() if code_match else ""

            print("📢 Action:", action)
            print("🧠 Code to run:\n", code)

            speak(action)
            run_safe_code(code)
        except Exception as e:
            print("❌ Code error:", e)
            speak("Code execute nahi ho paya.")
    else:
        speak("GPT se sahi code nahi mila. Kripya dobara koshish karein.")

# ---------- GUI Setup ----------
app = tk.Tk()
app.title("🤖 Hindi AI Assistant")
app.geometry("600x500")
app.config(bg="#1e1e1e")

tk.Label(app, text="🎤 Hindi Voice Assistant", font=("Arial", 20), bg="#1e1e1e", fg="white").pack(pady=10)

tk.Button(app, text="🎙️ Start Listening", font=("Arial", 16), bg="#4CAF50", fg="white", command=start_assistant).pack(pady=20)

user_command = tk.StringVar()
gpt_response = tk.StringVar()

tk.Label(app, textvariable=user_command, font=("Arial", 12), bg="#1e1e1e", fg="yellow", wraplength=550, justify="left").pack(pady=10)
tk.Label(app, textvariable=gpt_response, font=("Arial", 12), bg="#1e1e1e", fg="lightblue", wraplength=550, justify="left").pack(pady=10)

app.mainloop()
