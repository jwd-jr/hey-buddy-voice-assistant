import subprocess
import os

APPS = {
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "vs code": "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
    "vscode": "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "file explorer": "explorer.exe",
    "my pc": "explorer.exe",
    "spotify": "C:\\Users\\Lenovo\\AppData\\Roaming\\Spotify\\Spotify.exe",
    "word": "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
    "antigravity": "C:\\Users\\Lenovo\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Antigravity IDE"
}

def open_app(command):
    command = command.lower()
    for app_name, app_path in APPS.items():
        if app_name in command:
            try:
                if not os.path.exists(app_path) and not app_path.endswith(".exe"):
                    return f"Could not find {app_name} on this laptop"
                subprocess.Popen(app_path)
                print(f"✅ Opening {app_name}...")
                return f"Opening {app_name}"
            except Exception as e:
                print(f"❌ Error: {e}")
                return f"Could not open {app_name}"
    return "Sorry, I don't know that app!"