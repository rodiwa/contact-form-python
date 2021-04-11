# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

# Refs
# https://realpython.com/python-send-email/
# https://www.geeksforgeeks.org/send-mail-gmail-account-using-python/


import logging
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os


def main(name: str) -> str:
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
