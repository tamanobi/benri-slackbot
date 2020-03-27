from flask import Flask, request, jsonify
import requests
import json
import os
import feedparser
from dotenv import load_dotenv
import random

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
        if 'text' not in request.json['event']:
            return jsonify({})

        text = request.json['event']['text']

        user = event['user']
        RSS_URL = "https://b.hatena.ne.jp/hotentry/it.rss"

        d = feedparser.parse(RSS_URL)
        text = "\n".join([
            f"{entry.title}: {entry.link}" for entry in random.sample(d.entries, 3)
        ])
        payload = {"text": f"<@{user}> {text}"}
        res = requests.post(endpoint,data=json.dumps(payload))

    return jsonify({})
