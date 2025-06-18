import smtplib
import paramiko
from dotenv import load_dotenv
import os

load_dotenv()

hostname = os.getenv("HOSTNAME")
username = os.getenv("VM_USERNAME")
password = os.getenv("PASSWORD")
mail_file_path = os.getenv("PATH")
the_sender = 'brehovat'
the_receivers = ['tetiana']
the_message = """+++++++++++++++++++++
Subject: SMTP email example
This is a test message.
+++++++++++++++
"""

class TetianaBrekhova(object):

    def send_mail(ip, sender, receivers, message):
        smtpObj = smtplib.SMTP(ip)
        smtpObj.sendmail(sender, receivers, message)

    def read_mail_file(hostname, username, password, file_path):
       ssh = paramiko.SSHClient()
       ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
       ssh.connect(hostname,  port=22, username=username, password=password)
       stdin, stdout, stderr = ssh.exec_command('cat ' + file_path)
       output = stdout.read().decode('utf-8')
       ssh.close()
       return output

    def clean_mailbox(hostname, username, password, file_path):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, port=22, username=username, password=password)
        ssh.exec_command('> ' + file_path )
        ssh.close()
