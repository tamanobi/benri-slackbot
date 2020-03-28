from flask import Flask, request, jsonify
import requests
import json
import os
import feedparser
from dotenv import load_dotenv
import random

load_dotenv()
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def root_post():
    print(request)
    return jsonify(text="リクエスト成功")


@app.route("/listening", methods=["GET", "POST"])
def hear():
    # https://werkzeug.palletsprojects.com/en/0.15.x/wrappers/#werkzeug.wrappers.json.JSONMixin.get_json
    request_obj = request.get_json()
    if request_obj is None:
        return jsonify({})

    if "challenge" in request_obj:
        challenge_token = request_obj["challenge"]
        return jsonify(challenge=challenge_token)

    if "event" in request_obj:
        event = request_obj["event"]
        print(event)
        bot_id = event.get("bot_id")
        if bot_id is not None and bot_id == "B010WR2FE2C":
            return jsonify({})
        endpoint = os.environ["SLACK_WEBHOOK"]
        if "text" not in request_obj["event"]:
            return jsonify({})
        text = request_obj["event"]["text"]
        if "<@U010KB4S65R>" not in text:
            # メンションじゃない場合は無視する
            return jsonify({})
        if "占い" in text or "うらない" in text or "うらなって" in text or "占って":
            request_date = date.today().isoformat().replace("-", "/")
            fortune_endpoint = (
                f"http://api.jugemkey.jp/api/horoscope/free/{request_date}"
            )
            fortune_res = requests.get(fortune_endpoint)
            fortune = fortune_res.json()
            if fortune_res.status_code != 200 or fortune is None:
                payload = {"text": f"<@{user}> 占いに失敗しました"}
                requests.post(endpoint, data=json.dumps(payload))
                return jsonify({})

            # fortune["horoscope"]["2020/03/28"] をするコード
            sign_list = fortune.get("horoscope", {}).get(request_date, {})
            if sign_list == {}:
                payload = {"text": f"<@{user}> 占いに失敗しました"}
                requests.post(endpoint, data=json.dumps(payload))
                return jsonify({})

            messages = [sign["sign"] + ": " + sign["content"] for sign in sign_list]
            message.append("powerd by JugemKey")
            message.append("【PR】原宿占い館 塔里木")

            payload = {"text": "\n".join(messages)}
            res = requests.post(endpoint, data=json.dumps(payload))
            return jsonify({})

        user = event["user"]
        RSS_URL = "https://b.hatena.ne.jp/hotentry/it.rss"

        d = feedparser.parse(RSS_URL)
        text = "\n".join(
            [f"{entry.title}: {entry.link}" for entry in random.sample(d.entries, 3)]
        )
        payload = {"text": f"<@{user}> {text}"}
        res = requests.post(endpoint, data=json.dumps(payload))

    return jsonify({})
