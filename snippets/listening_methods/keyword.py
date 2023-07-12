import pyttsx3
import speech_recognition as sr

# Prepare Text to Speech
tts = pyttsx3.init()
voices = tts.getProperty('voices')
tts.setProperty('voice', voices[1].id)

# Prepare Microphone
listener = sr.Recognizer()
listener.non_speaking_duration = 0
rate = 48000  # Default is 16000
listener.energy_threshold = 1000  # Manually adjust threshold


def listen_for_keyword(keyword: str):
    while True:
        with sr.Microphone(sample_rate=48000) as source:
            print("Listening...")
            try:
                audio = listener.listen(source, phrase_time_limit=5.0)  # Set the timeout value to 1 second
                print("...not listening")
            except:
                print("NO AUDIO")
                print("...not listening")

        try:
            text = listener.recognize_google(audio)
            print(text)

            if keyword in text:
                print("KEY WORD")

        except sr.WaitTimeoutError:
            print("Timeout")

        except sr.UnknownValueError:
            print("Could not understand audio.")

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))


if __name__ == "__main__":
    listen_for_keyword("hey")

# recognize_sphinx for offline detection?
