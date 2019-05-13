import defang
import json
import requests
from api import app

def send_to_slack(slack_msg):
    # Add URL Defanging to prevent slack crawl.
    data = {
        'text': slack_msg,
        'username': 'Denzel Phish Detector',
        'icon_emoji': ':male-detective:'
    }

    response = requests.post(app.config['SLACK_WEBHOOK'], data=json.dumps(
        data), headers={'Content-Type': 'application/json'})

    print('Response: ' + str(response.text))
    print('Response code: ' + str(response.status_code))
