import requests
import json
import os

endpoint = os.environ['SLACK_WEBHOOK']
payload = {"text":"Slack Appsのテストです。環境変数を使うべき！"}
res = requests.post(endpoint,data=json.dumps(payload))

if res.status_code == 200:
    print(res.content)
