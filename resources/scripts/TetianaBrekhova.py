import smtplib
import paramiko


def send_mail(ip, sender, receivers, message):
    smtpObj = smtplib.SMTP(ip)
    smtpObj.sendmail(sender, receivers, message)

def clean_mailbox(hostname, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, port=22, username=username, password=password)
    ssh.exec_command('> /var/mail/{user}'.format(user=username))
    ssh.close()

def read_mail_file(hostname, username, password):
   ssh = paramiko.SSHClient()
   ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
   ssh.connect(hostname,  port=22, username=username, password=password)
   stdin, stdout, stderr = ssh.exec_command('cat  /var/mail/{user}'.format(user=username))
   output = stdout.read().decode('utf-8')
   ssh.close()
   return output

def get_mail_list(hostname, username, password):
    mail_text = read_mail_file(hostname, username, password)
    mail_list = mail_text.split("\n\nFrom")
    return mail_list
