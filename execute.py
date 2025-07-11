import webbrowser
import os
import shutil
import winshell

def run_safe_code(code):
    try:
        safe_globals = {
            "webbrowser": webbrowser,
            "os": os,
            "shutil": shutil,
            "winshell": winshell
        }
        exec(code, safe_globals)
    except Exception as e:
        print("❌ Execution Error:", e)
