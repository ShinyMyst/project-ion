import pyttsx3
import speech_recognition as sr
import openai
from api import key

class SpeechRecognition:
    def __init__(self, properties):
        # Set property values
        self.energy_threshold = properties[0]
        self.sample_rate = properties[1]
        self.adjust_for_ambient_noise = properties[2]
        self.non_speaking_duration = properties[3]
        self.timeout = properties[4]
        self.phrase_time_limit = properties[5]
        # Prep Modules
        self._prep_recognizer()
        self._prep_voice()
        self._prep_ai()
        # Begin listening for input
        self._listen()

    def _prep_recognizer(self):
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = self.energy_threshold
        self.recognizer.non_speaking_duration = self.non_speaking_duration

    def _prep_voice(self):
        tts = pyttsx3.init()
        voices = tts.getProperty('voices')
        tts.setProperty('voice', voices[1].id)

    def _prep_ai(self):
        openai.api_key = key
        model = "text-davinci-002"  # Ada

    def _listen(self):
        while True:
            with sr.Microphone(sample_rate=self.sample_rate) as source:
                print("Listening...")
                audio = self.recognizer.listen(source, timeout=self.timeout, phrase_time_limit=self.phrase_time_limit)

            try:
                text = self.recognizer.recognize_google(audio)
                process_text(text)

            except sr.UnknownValueError:
                chat("Could not understand audio.")

            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))







"""
listener.non_speaking_duration = 0.5
rate = 48000  # Default is 16000
listener.energy_threshold = 1000  # Manually adjust threshold"""

# Prepare OpenAi


def gpt_response(prompt: str):
    completions = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,)

    message = completions.choices[0].text.strip()
    return message


def process_text(text):
    text.lower()
    print("You said:", text)

    # Conditions
    if "please" in text.lower():
        response = gpt_response(text)
        chat(response)
    elif "cat" in text.lower():
        chat("MEOW")
    elif "dog" in text.lower():
        chat("BARK")
    else:
        chat("I don't know what you're talking about.")


def chat(message: str):
    tts.say(message)
    print(message)
    tts.runAndWait()


