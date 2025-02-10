import speech_recognition as sr

def listen_for_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something... 🎤")
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"Recognized: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
        return None
    except sr.RequestError:
        print("Could not request results. Check internet connection.")
        return None
