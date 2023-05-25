import speech_recognition as sr
import pyttsx3

# Initialize the speech recognition engine
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_audio(duration):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")

        # Adjust microphone energy threshold to ambient noise levels
        r.adjust_for_ambient_noise(source)

        try:
            # Listen to the user's input
            audio = r.listen(source, timeout=duration)
        except sr.WaitTimeoutError:
            # Handle timeout error
            print("Timeout reached. No speech detected.")
            return ""

        try:
            text = r.recognize_google(audio)
            print("Recognized Text:", text)
            return text
        except sr.UnknownValueError:
            # Handle speech recognition error
            print("Unable to recognize speech.")
            return ""

        except sr.RequestError as e:
            # Handle speech recognition service error
            print("Error occurred; {0}".format(e))
            return ""

def main(duration):
    while True:
        text = get_audio(duration).lower()
        if "hello" in text:
            speak("Hi there!")
        elif "how are you" in text:
            speak("I'm doing well, thank you for asking.")
        elif "goodbye" in text:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I didn't understand what you said.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    duration = 5
    main(duration)

