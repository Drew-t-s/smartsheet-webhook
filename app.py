import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

GITHUB_TOKEN = os.environ["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"]
GITHUB_OWNER = os.environ["Drew-t-s"]
GITHUB_REPO = os.environ["Test-TOA"]

@app.route("/smartsheet-webhook", methods=["POST"])
def webhook():

    # Smartsheet verification challenge
    challenge = request.headers.get("Smartsheet-Hook-Challenge")
    if challenge:
        return jsonify({
            "smartsheetHookResponse": challenge
        }), 200

    payload = {
        "event_type": "smartsheet_changed"
    }

    requests.post(
        f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/dispatches",
        headers={
            "Authorization": f"Bearer {GITHUB_TOKEN}",
            "Accept": "application/vnd.github+json"
        },
        json=payload
    )

    return "", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
