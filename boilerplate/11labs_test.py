import requests
import api


def read_message(message):
    url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"

    headers = {
      "Accept": "audio/mpeg",
      "Content-Type": "application/json",
      "xi-api-key": api.lab_key
    }

    data = {
      "text": message,
      "model_id": "eleven_monolingual_v1",
      "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.5
      }
    }

    response = requests.post(url, json=data, headers=headers)
    print(response.status_code)
    with open('output.mp3', 'wb') as f:
        f.write(response.content)


read_message("Insert Text Here")
