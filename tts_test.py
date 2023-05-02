import pyttsx3

# Create a TTS engine
engine = pyttsx3.init()

# Set the voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Say a message
engine.say("Hello, world!")

# Run the engine
engine.runAndWait()
