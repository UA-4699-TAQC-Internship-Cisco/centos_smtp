import paramiko
import os


from dotenv import load_dotenv
from pycparser.ply.yacc import resultlimit

load_dotenv()



def read_mail(hostname=None, username=None, password=None):

    hostname = hostname or os.getenv("HOSTNAME")
    username = username or os.getenv("SSH_USERNAME")
    password = password or os.getenv("PASSWORD")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, username=username, password=password)

    command = "cat /var/mail/{}".format(username)

    stdin, stdout, stderr = ssh.exec_command(command)

    output = stdout.read().decode()


    ssh.close()

    return output

