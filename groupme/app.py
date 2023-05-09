import os
import sys
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request


app = Flask(__name__)


@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    log('Recieved {}'.format(data))
    name = data['name']
    parse = data['text']
    sentence = parse.lower()
    response = create_response(sentence)
    if response:
        if name != "Iona":
            send_message(response)
    return "ok", 200


def send_message(msg):
    url = 'https://api.groupme.com/v3/bots/post'

    data = {
          'bot_id': os.getenv('GROUPME_BOT_ID'),
          'text': msg,
         }
    request = Request(url, urlencode(data).encode())
    urlopen(request).read().decode()


def create_response(sentence):
    msg = {}
    if sentence == "test":
        msg = "This is working"
    return msg


def log(msg):
    print(str(msg))


sys.stdout.flush()

# Reference
# https://github.com/DarthSergeant/elysium-bot/tree/master
