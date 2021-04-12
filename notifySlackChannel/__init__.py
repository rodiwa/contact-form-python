import logging
import requests
import os
import datetime
import pytz


def notifySlack(name: str):
    """To notify slack channel that a new message is received."""
    IST = pytz.timezone('Asia/Calcutta')

    SLACK_URL = os.environ["SLACK_URL"]
    SLACK_ICON_URL = os.environ["SLACK_ICON_URL"]
    SLACK_ICON_EMOJI = os.environ["SLACK_ICON_EMOJI"]
    SLACK_BOT_NAME = os.environ["SLACK_BOT_NAME"]

    user_name = name['user_name']
    message = name['message']
    email = name['email']
    formattedDate = datetime.datetime.now(IST).strftime("%a, %b %d")
    formattedTime = datetime.datetime.now(IST).strftime("%r")
    formattedMessage = f"{user_name} ({email}) said \"{message}\" on {formattedDate} at {formattedTime}."
    payload = {
        "blocks": [
              {
                  "type": "section",
                  "text": {
                      "type": "mrkdwn",
                          "text": formattedMessage
                  }
              }
        ]
    }
    response = requests.post(SLACK_URL, json=payload)
    return response.status_code


def main(name: str) -> str:
    status_code = notifySlack(name)
    return status_code
