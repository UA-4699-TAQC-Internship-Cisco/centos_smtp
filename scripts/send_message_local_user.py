import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

def send_mail(from_addr, to_addrs,  body, subject = None, host = None, port = None):
    host = host or os.getenv("HOSTNAME")
    port = port or os.getenv("SMTP_PORT")

    if isinstance(to_addrs, str):
        to_addrs = [to_addrs]

    lines = [
        "From: {}".format(from_addr),
        "To: {}".format(', '.join(to_addrs)),
        "Subject: {}".format(subject),
        "",
        body
    ]

    msg = "\r\n".join(lines)


    server = smtplib.SMTP(host, port)
    server.set_debuglevel(1)
    server.sendmail(from_addr, to_addrs, msg)
    server.quit()

