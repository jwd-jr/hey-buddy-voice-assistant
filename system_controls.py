import os
import subprocess

def system_control(command):
    command = command.lower()
    
    if "shutdown" in command:
        speak_text = "Okay! Shutting down your laptop. Goodbye!"
        print(speak_text)
        os.system("shutdown /s /t 5")
        return speak_text
    
    elif "sleep" in command:
        speak_text = "Putting your laptop to sleep. Goodnight!"
        print(speak_text)
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        return speak_text
    
    elif "restart" in command:
        speak_text = "Restarting your laptop. See you soon!"
        print(speak_text)
        os.system("shutdown /r /t 5")
        return speak_text
    
    elif "sign out" in command or "logout" in command:
        speak_text = "Signing out. Goodbye!"
        print(speak_text)
        os.system("shutdown /l")
        return speak_text
    
    return None

if __name__ == "__main__":
    print(system_control("sleep"))