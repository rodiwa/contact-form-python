# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import requests
import os
import datetime
import pytz


def notifySlack(name: str):
    # test

    # test till here

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
              },
            {
                  "type": "actions",
                  "elements": [
                      {
                          "type": "button",
                          "text": {
                              "type": "plain_text",
                              "text": "Send Auto Reply",
                                  "emoji": True
                          },
                          "value": "click_me_123",
                          "action_id": "actionId-0"
                      }
                  ]
              }
        ]
    }
    response = requests.post(SLACK_URL, json=payload)
    return response.status_code


def main(name: str) -> str:
    status_code = notifySlack(name)
    return status_code
