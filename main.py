import pyttsx3
import speech_recognition as sr
import openai
from api import key

# Prepare Text to Speech
tts = pyttsx3.init()
voices = tts.getProperty('voices')
tts.setProperty('voice', voices[1].id)

# Prepare Microphone
listener = sr.Recognizer()
listener.non_speaking_duration = 0.5
rate = 48000  # Default is 16000
listener.energy_threshold = 1000  # Manually adjust threshold

# Prepare OpenAi
openai.api_key = key
model = "text-davinci-002"  # Ada


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


def main():
    listening = True
    while listening:
        with sr.Microphone(sample_rate=48000) as source:
            print("Listening...")
            audio = listener.listen(source)

        try:
            text = listener.recognize_google(audio)
            process_text(text)

        except sr.UnknownValueError:
            chat("Could not understand audio.")

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))


if __name__ == "__main__":
    main()
