import time
import requests

# Replace this with your actual Slack webhook when ready
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/YOUR/WEBHOOK/HERE"

messages = [
    "Trump says 60% tariffs are coming for Chinese EVs",
    "Trump plans to replace Powell",
    "Trump tweets about fake news CNN",
    "Trump calls for more oil drilling",
    "Trump mentions golf tournament"
]

keywords = ["tariff", "China", "oil", "sanction", "interest", "Powell", "border", "EV"]

def send_to_slack(text):
    payload = {"text": f"🚨 Trump Alert: {text}"}
    requests.post(SLACK_WEBHOOK_URL, json=payload)

def check():
    for msg in messages:
        if any(word in msg.lower() for word in keywords):
            send_to_slack(msg)

check()
