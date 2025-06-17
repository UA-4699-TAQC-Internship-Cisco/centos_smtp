import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

hostname = os.getenv("HOSTNAME")
the_sender = 'brehovat'
the_receiver = ['tetiana']
the_message = """+++++++++++++++++++++
Subject: SMTP email example
This is a test message.
+++++++++++++++
"""


def send_mail(ip_hostname, sender, receivers, message):
    smtpObj = smtplib.SMTP(ip_hostname)
    smtpObj.sendmail(sender, receivers, message)
    print "Successfully sent email"


# send_mail(hostname, the_sender, the_receiver, the_message)
