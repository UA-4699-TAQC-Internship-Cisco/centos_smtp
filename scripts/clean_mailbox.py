import paramiko
from dotenv import load_dotenv
import os

load_dotenv()

hostname = os.getenv("HOSTNAME")
username = os.getenv("VM_USERNAME")
password = os.getenv("PASSWORD")
path = "/var/mail/tetiana"


def clean_mailbox(hostname, username, password, file_path):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, port=22, username=username, password=password)
    ssh.exec_command('> ' + file_path )
    stdin, stdout, stderr = ssh.exec_command('cat ' + file_path)
    output = stdout.read().decode('utf-8')
    print output
    ssh.close()


# clean_mailbox(hostname, username, password, path)
