import os
import api
import openai


openai.api_key = api.key
audio_file = open("sample.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
print(transcript.text)

