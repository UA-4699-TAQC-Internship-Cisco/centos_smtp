import logging
import os
import smtplib

import dotenv
import paramiko
from email.mime.text import MIMEText

dotenv.load_dotenv()

logging.basicConfig(
    filename='../logs/yuliashap_log.txt',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


class MailClient:
    def __init__(self):
        self.host = os.getenv("SSH_HOST")
        self.port = int(os.getenv("SSH_PORT", 22))
        self.username = os.getenv("SSH_USERNAME")
        self.password = os.getenv("SSH_PASSWORD")
        self.mail_file = os.getenv("EMAIL_DIR")
        self.smtp_ip = os.getenv("SERVER_IP")
        self.smtp_port = int(os.getenv("SERVER_PORT", 25))
        self.sender = os.getenv("LOCAL_SENDER")
        self.recipient = os.getenv("REMOTE_RECIPIENT")
        self.subject = os.getenv("EMAIL_SUBJECT")
        self.body = os.getenv("EMAIL_BODY")

    def send_email(self):
        msg = MIMEText(self.body)
        msg['Subject'] = self.subject
        msg['From'] = self.sender
        msg['To'] = self.recipient

        try:
            server = smtplib.SMTP(self.smtp_ip, self.smtp_port)
            server.sendmail(self.sender, [self.recipient], msg.as_string())
            server.quit()
            logging.info("Email sent from %s to %s", self.sender, self.recipient)
        except Exception as e:
            logging.error("Failed to send email: %s", str(e))

    def read_all_emails(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.host, port=self.port, username=self.username, password=self.password)

        _, stdout, _ = ssh.exec_command("cat {}".format(self.mail_file))
        content = stdout.read().decode('utf-8', 'ignore')
        ssh.close()

        messages = content.split("From ")[1:]
        parsed_emails = []

        for msg in messages:
            lines = msg.strip().split("\n")
            frm = next((line[5:].strip() for line in lines if line.lower().startswith("from:")), "")
            subj = next((line[8:].strip() for line in lines if line.lower().startswith("subject:")), "")
            try:
                body = " ".join(lines[lines.index("") + 1:])[:100]
            except ValueError:
                body = ""

            logging.info("From: %s", frm)
            logging.info("Subject: %s", subj)
            logging.info("Body snippet: %s", body)
            logging.info("-" * 40)

            parsed_emails.append({'from': frm, 'subject': subj, 'body': body})

        return parsed_emails

    def get_last_email(self):
        emails = self.read_all_emails()
        if emails:
            last = emails[-1]
            logging.info("Last email fetched - From: %s | Subject: %s | Body: %s", last['from'], last['subject'],
                         last['body'])
            return last
        else:
            logging.warning("No emails found in the mailbox.")
            return None


if __name__ == "__main__":
    client = MailClient()
    client.send_email()
    client.get_last_email()
