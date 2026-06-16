import os
from speaker import speak
import speech_recognition as sr

recognizer = sr.Recognizer()

def listen_confirmation():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening for confirmation...")
        try:
            audio = recognizer.listen(source, timeout=5)
            return recognizer.recognize_google(audio).lower()
        except:
            return ""

def system_control(command):
    command = command.lower()

    if "shutdown" in command or "power off" in command:
        speak("Are you sure you want to shutdown?")
        confirm = listen_confirmation()
        if "yes" in confirm:
            speak("Okay! Shutting down. Goodbye Jaidie!")
            os.system("shutdown /s /t 5")
        else:
            speak("Okay! Shutdown cancelled!")

    elif "sleep" in command:
        speak("Are you sure you want to sleep?")
        confirm = listen_confirmation()
        if "yes" in confirm:
            speak("Putting laptop to sleep. Goodnight Jaidie!")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        else:
            speak("Okay! Sleep cancelled!")

    elif "restart" in command:
        speak("Are you sure you want to restart?")
        confirm = listen_confirmation()
        if "yes" in confirm:
            speak("Restarting laptop. See you soon Jaidie!")
            os.system("shutdown /r /t 5")
        else:
            speak("Okay! Restart cancelled!")

    elif "sign out" in command or "logout" in command:
        speak("Are you sure you want to sign out?")
        confirm = listen_confirmation()
        if "yes" in confirm:
            speak("Signing out. Goodbye Jaidie!")
            os.system("shutdown /l")
        else:
            speak("Okay! Sign out cancelled!")