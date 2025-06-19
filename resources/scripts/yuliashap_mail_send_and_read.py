import os
import smtplib
from email.mime.text import MIMEText

import dotenv
import paramiko

from resources.data.logger_config import setup_logger

dotenv.load_dotenv()
logger = setup_logger()


def send_email(sender, recipient, subject, body, server_ip, server_port):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    try:
        server = smtplib.SMTP(server_ip, server_port)
        server.sendmail(sender, [recipient], msg.as_string())
        server.quit()
        logger.info("Email sent from %s to %s", sender, recipient)
    except Exception as e:
        logger.error("Failed to send email: %s", str(e))


def read_all_emails(host, port, username, password, mail_file):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, port=port, username=username, password=password)

    _, stdout, _ = ssh.exec_command("cat {}".format(mail_file))
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

        logger.info("From: %s", frm)
        logger.info("Subject: %s", subj)
        logger.info("Body snippet: %s", body)
        logger.info("-" * 40)

        parsed_emails.append({'from': frm, 'subject': subj, 'body': body})

    logger.info(parsed_emails)
    return parsed_emails


def get_last_email(host, port, username, password, mail_file):
    emails = read_all_emails(host, port, username, password, mail_file)
    if emails:
        last = emails[-1]
        logger.info("Last email fetched - From: %s | Subject: %s", last['from'], last['subject'])
        return last
    else:
        logger.warning("No emails found in the mailbox.")
        return None


if __name__ == "__main__":
    send_email(
        sender=os.getenv("LOCAL_SENDER"),
        recipient=os.getenv("REMOTE_RECIPIENT"),
        subject=os.getenv("EMAIL_SUBJECT"),
        body=os.getenv("EMAIL_BODY"),
        server_ip=os.getenv("SERVER_IP"),
        server_port=int(os.getenv("SERVER_PORT", 25))
    )

    get_last_email(
        host=os.getenv("SSH_HOST"),
        port=int(os.getenv("SSH_PORT", 22)),
        username=os.getenv("SSH_USERNAME"),
        password=os.getenv("SSH_PASSWORD"),
        mail_file=os.getenv("EMAIL_DIR")
    )
