from flask import Flask, request, jsonify
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def root_post():
    print(request)
    challenge_token = request.json['challenge']
    return jsonify(challenge=challenge_token)

@app.route('/listening', methods=['GET', 'POST'])
def hear():
    if 'challenge' in request.json:
        challenge_token = request.json['challenge']
        return jsonify(challenge=challenge_token)

    if 'event' in request.json:
        event = request.json['event']
        print(event)
        bot_id = event.get('bot_id')
        if bot_id is not None and bot_id == 'B010WR2FE2C':
            return jsonify({})
        endpoint = os.environ['SLACK_WEBHOOK']
        text = request.json['event']['text']

        user = event['user']
        # メンションをし返す
        text = text.replace('<@U010KB4S65R>', f"<@{user}>")

        payload = {"text":text}
        res = requests.post(endpoint,data=json.dumps(payload))

    return jsonify({})
