import time
import requests

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
    try:
        response = requests.post(SLACK_WEBHOOK_URL, json=payload)
        print(f"✅ Sent to Slack: {text} | Status: {response.status_code}")
        print(f"Response content: {response.text}")
    except Exception as e:
        print(f"❌ Slack error: {e}")

def check():
    for msg in messages:
        if any(word in msg.lower() for word in keywords):
            send_to_slack(msg)

send_to_slack("🚨 Test message: Fox News bot is live!")
check()

print("✅ Script completed. Sleeping to keep logs open...")
time.sleep(15)
