# Refs
# https://realpython.com/python-send-email/
# https://www.geeksforgeeks.org/send-mail-gmail-account-using-python/
# https://app.mailjet.com/auth/get_started/developer


# import smtplib
# import ssl
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
import logging
from mailjet_rest import Client
import os


def sendGmail(name: str) -> str:
    """To send mail using Python SMTP."""
    u = os.environ["EMAIL_USR"]
    p = os.environ["EMAIL_PWD"]
    smtp_server = os.environ["EMAIL_SMTP_SRVR"]
    from_email = u
    to_email = name['email']

    message = MIMEMultipart("alternative")
    message["Subject"] = "Rohit's bot at your service!"
    message["From"] = from_email
    message["To"] = to_email

    text = """\
    Thank you for checking out the website. Please connect on LinkedIn and we can take things forward.
    """
    html = """\
    <html>
      <body>
        <p>Thank you for checking out the website. Please connect on <a href="https://in.linkedin.com/in/rohitdiwakar">LinkedIn</a> and we can take things forward.</p>
        <p>Cheers, <br>Rohit's Bot<p>
      </body>
    </html>
    """

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, 465, context=context) as server:
        server.login(from_email, p)
        server.sendmail(
            from_email, to_email, message.as_string()
        )

    return


def sendSMTPRelay(name: str) -> str:
    """To send mail using SMTP Relay Mailjet service."""
    API_KEY = os.environ["MAILJET_API_KEY"]
    API_SECRET = os.environ["MAILJET_API_SECRET"]
    FROM_EMAIL = os.environ["MAILJET_FROM_EMAIL"]
    FROM_EMAIL_USER = os.environ["MAILJET_FROM_EMAIL_NAME"]
    TO_EMAIL = name['email']
    TO_EMAIL_USER = name['user_name'].title()

    EMAIL_SUBJECT = "Rohit's bot at your service!"
    EMAIL_TEXT = "Rohit says hello!"
    EMAIL_HTML_CONTENT = """\
    <html>
      <body>
        <p>Thank you for checking out the website. Please connect on <a href="https://in.linkedin.com/in/rohitdiwakar">LinkedIn</a> and we can take things forward.</p>
        <p>Cheers, <br>Rohit's Bot<p>
      </body>
    </html>
    """

    mailjet = Client(auth=(API_KEY, API_SECRET), version='v3.1')
    data = {
        'Messages': [
            {
                "From": {
                    "Email": FROM_EMAIL,
                    "Name": FROM_EMAIL_USER
                },
                "To": [
                    {
                        "Email": TO_EMAIL,
                        "Name": TO_EMAIL_USER
                    }
                ],
                "Subject": EMAIL_SUBJECT,
                "TextPart": EMAIL_TEXT,
                "HTMLPart": EMAIL_HTML_CONTENT,
                "CustomID": "AppGettingStartedTest"
            }
        ]
    }
    result = mailjet.send.create(data=data)
    return True


def main(name: str) -> str:
    email_response = sendSMTPRelay(name)
    return email_response
