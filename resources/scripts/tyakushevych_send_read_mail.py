import smtplib
import os
import paramiko
from dotenv import load_dotenv

load_dotenv()


def send_mail(host, port, from_addr, to_addrs, body, subject=None):
    """
    :param host:
    :param port:
    :param from_addr:
    :param to_addrs:
    :param body:
    :param subject:
    :return:
    """

    lines = [
        "From: {}".format(from_addr),
        "To: {}".format(', '.join(to_addrs)),
        "Subject: {}".format(subject),
        "",
        body
    ]

    msg = "\r\n".join(lines)

    server = smtplib.SMTP(host, int(port))
    server.set_debuglevel(1)
    result = server.sendmail(from_addr, to_addrs, msg)
    server.quit()
    return result




def read_mail(hostname, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, username=username, password=password)

    command = "cat /var/mail/{}".format(username)

    _, stdout, _ = ssh.exec_command(command)

    output = stdout.read().decode()

    ssh.close()



    return output


hostname = os.getenv("HOSTNAME")
port = int(os.getenv("SMTP_PORT"))
username = os.getenv("SSH_USERNAME")
password = os.getenv("PASSWORD")
from_addr = "root@localhost"
to_addrs = ["user1@localhost"]
subject = "Test subject"
body = "Test helper function"





