import os
import smtplib

import dotenv
from email.mime.text import MIMEText

import config

dotenv.load_dotenv()


def send_email(sender=None, recipient=None, subject=None, body=None, server_ip=None, server_port=None):
    sender = sender or os.getenv("LOCAL_SENDER")
    recipient = recipient or os.getenv("REMOTE_RECIPIENT")
    subject = subject or config.EMAIL_SUBJECT
    body = body or config.EMAIL_BODY
    server_ip = server_ip or os.getenv("SERVER_IP")
    server_port = server_port or int(os.getenv("SERVER_PORT", 25))

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    server = smtplib.SMTP(server_ip, server_port)
    server.sendmail(sender, [recipient], msg.as_string())
    server.quit()


if __name__ == "__main__":
    send_email()
