import subprocess

APPS = {
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "vs code": "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
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
                subprocess.Popen(app_path)
                print(f"✅ Opening {app_name}...")
                return f"Opening {app_name}"
            except Exception as e:
                print(f"❌ Could not open {app_name}: {e}")
                return f"Could not open {app_name}"
    return "App not found"

if __name__ == "__main__":
    print(open_app("open chrome"))
    print(open_app("open spotify"))
    print(open_app("open word"))
    print(open_app("open vscode"))
    print(open_app("open calculator"))