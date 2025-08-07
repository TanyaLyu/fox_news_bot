import time
import requests

# Replace this with your actual Slack webhook when ready
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"

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
send_to_slack("🚨 Test message: Fox News bot is live!")
check()
