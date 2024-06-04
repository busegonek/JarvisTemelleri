import speech_recognition as sr
import pyttsx3

# Create recognizer for speech input
recognizer = sr.Recognizer()

# Create engine for speech output
engine = pyttsx3.init()

# Set speech rate (words per minute)
engine.setProperty('rate', 150)  # Adjust this value as needed

def recognize_speech():
    with sr.Microphone() as source:
        print("I'm ready for Jarvis, waiting for a command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Speech input detected, processing...")
        command = recognizer.recognize_google(audio)  # Google Speech API
        print("Recognized command: " + command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, speech could not be understood.")
        return ""
    except sr.RequestError:
        print("Google Speech API could not be reached. Using offline speech recognition...")
        return recognize_sphinx()  # Fallback to Sphinx for offline recognition

def recognize_sphinx():
    with sr.Microphone() as source:
        print("Using offline speech recognition. Speak now...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Speech input detected, processing...")
        command = recognizer.recognize_sphinx(audio)  # Sphinx for offline recognition
        print("Recognized command: " + command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, speech could not be understood.")
        return ""

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        command = recognize_speech()

        if "jarvis" in command:
            speak("i have to check something . Please enter the password from the keyboard.")

            password = input("Enter the password: ")

            if password == "password123":  # Use your actual password here
                speak("Welcome my darling, Zeus. how can i help you my beautiful amazing owner")
            else:
                speak("Sorry, wrong password. Please try again.")
