import speech_recognition as sr

recognizer = sr.Recognizer()

print("Hey Buddy is listening... Say 'Hey Buddy' to wake me up!")

while True:
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Waiting...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio).lower()
        print("Heard:", text)

        if "hey buddy" in text:
            print("✅ Wake word detected! I am awake!")
            print("What is your command?")
            # We will add commands here next
            break

    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        print("Internet error")