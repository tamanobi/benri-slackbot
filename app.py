from flask import Flask, request, jsonify

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
        text = request.json['event']['text']
        print(text)

    return jsonify({})
