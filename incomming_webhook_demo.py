import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
endpoint = os.environ['SLACK_WEBHOOK']
payload = {"text":".envから読み込める"}
res = requests.post(endpoint,data=json.dumps(payload))

if res.status_code == 200:
    print(res.content)
