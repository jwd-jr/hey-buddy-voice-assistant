import speech_recognition as sr

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
        print("📧 Opening Gmail checker...")
    elif "open chrome" in command:
        print("🌐 Opening Chrome...")
    elif "open vs code" in command:
        print("💻 Opening VS Code...")
    elif "shutdown" in command:
        print("🔴 Shutting down...")
    elif "sleep" in command:
        print("😴 Going to sleep...")
    else:
        print("❓ Command not recognized:", command)

print("👂 Hey Buddy is listening... Say 'Hey Buddy'!")

while True:
    print("Waiting...")
    text = listen()
    print("Heard:", text)

    if "hey buddy" in text:
        print("✅ Wake word detected! What is your command?")
        command = listen()
        print("Command:", command)
        handle_command(command)