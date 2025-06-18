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
    datefmt='%Y-%m-%d %H:%M:%S')


def send_email(sender, recipient, subject, body, server_ip, server_port):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    server = smtplib.SMTP(server_ip, server_port)
    server.sendmail(sender, [recipient], msg.as_string())
    logging.info("Email sent from %s to %s", sender, recipient)
    server.quit()


def read_emails(host, port, username, password, mail_file):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, port=port, username=username, password=password)

    _, stdout, _ = ssh.exec_command("cat {}".format(mail_file))
    content = stdout.read().decode('utf-8', 'ignore')

    for msg in content.split("From ")[1:]:
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

    ssh.close()


if __name__ == "__main__":
    send_email(
        sender=os.getenv("LOCAL_SENDER"),
        recipient=os.getenv("REMOTE_RECIPIENT"),
        subject=os.getenv("EMAIL_SUBJECT"),
        body=os.getenv("EMAIL_BODY"),
        server_ip=os.getenv("SERVER_IP"),
        server_port=int(os.getenv("SERVER_PORT", 25)))
    read_emails(
        host=os.getenv("SSH_HOST"),
        port=int(os.getenv("SSH_PORT", 22)),
        username=os.getenv("SSH_USERNAME"),
        password=os.getenv("SSH_PASSWORD"),
        mail_file=os.getenv("EMAIL_DIR"))
