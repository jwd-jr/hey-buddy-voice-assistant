import speech_recognition as sr
from speaker import speak
from gmail_checker import fetch_emails
from groq_summarizer import summarize_emails
from app_opener import open_app
from system_controls import system_control

recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio).lower()
    except:
        return ""

def handle_command(command):
    if "email" in command or "gmail" in command:
        speak("Sure! Let me check your emails!")
        emails = fetch_emails()
        summary = summarize_emails(emails)
        speak(summary)

    elif "open" in command:
        result = open_app(command)
        speak(result)

    elif "shutdown" in command or "sleep" in command or "restart" in command:
        system_control(command)

    else:
        speak("Sorry, I did not understand that command!")

# Main loop
speak("Hello!  Jaidie, How are you !")

while True:
    print("Waiting for wake word...")
    text = listen()

    if "beta" in text:
        speak("Yes! jaidie I am here")
        command = listen()
        print("Command:", command)
        handle_command(command)