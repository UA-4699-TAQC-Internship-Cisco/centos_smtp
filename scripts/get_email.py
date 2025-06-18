# !/usr/bin/env python2
# -*- coding: utf-8 -*-

# !/usr/bin/env python2
import imaplib
import email
import os
from email.header import decode_header
from dotenv import load_dotenv

load_dotenv()

server = os.getenv("IMAP_SERVER")
user = os.getenv("EMAIL_ACCOUNT")
password = os.getenv("EMAIL_PASSWORD")

try:
    mail = imaplib.IMAP4_SSL(server, 993)
    mail.login(user, password)
    mail.select("inbox")

    status, ids = mail.search(None, "ALL")
    message_ids = ids[0].split()
    print("Letters in box:", len(message_ids))

except Exception as e:
    print("Error:", str(e))
finally:
    if 'mail' in locals():
        mail.logout()
