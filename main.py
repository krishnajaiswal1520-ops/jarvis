import speech_recognition as sr
import webbrowser
import pyttsx3

# Initialize recognizer & engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    command = command.lower()

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif "exit" in command or "stop" in command:
        speak("Goodbye")
        exit()

    else:
        speak("Sorry, I don't understand that command")

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

    return recognizer.recognize_google(audio)

if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        try:
            print("Say wake word...")
            word = listen().lower()

            if "Nakul" in word:
                speak("Yes, tell me")
                
                try:
                    command = listen().lower()
                    processCommand(command)
                except sr.UnknownValueError:
                    speak("I didn't understand the command")

        except sr.WaitTimeoutError:
            continue
        except sr.UnknownValueError:
            print("Wake word not understood")
        except Exception as e:
            print("Error:", e)
