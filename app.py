from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'いえーい、見てる？'

@app.route('/', methods=['POST'])
def root_post():
    challenge_token = request.json['challenge']
    return jsonify(challenge=challenge_token)
