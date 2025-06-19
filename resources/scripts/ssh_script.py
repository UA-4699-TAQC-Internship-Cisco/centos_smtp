import paramiko


def read_mail(hostname, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, username=username, password=password)

    command = "cat /var/mail/{}".format(username)

    _, stdout, _ = ssh.exec_command(command)

    output = stdout.read().decode()

    ssh.close()

    return output
