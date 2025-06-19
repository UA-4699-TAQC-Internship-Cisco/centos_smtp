import smtplib
import paramiko


def connect_server(host, port = 25):
    try:
        smtp_server = smtplib.SMTP(host)
        return smtp_server
    except smtplib.SMTPServerDisconnected:
        print "Cannot connect to Server, check the Host"

def send_message_smtp(from_addr, to_addr, message, smtp_srv = smtplib.SMTP()):
    try:
        smtp_srv.verify(to_addr)
        smtp_srv.sendmail(from_addr, to_addr, message)
    except smtplib.SMTPRecipientsRefused:
        print 'Address of the destination is Not valid'
    finally:
        smtp_srv.quit()

def check_smtp_mail(username, password, hostname):
    session = paramiko.SSHClient()
    session.load_system_host_keys()
    session.connect(hostname, 22, username, password)
    _, stdout, _ = session.exec_command("cat /home/{}/Maildir/new/*".format(username))

    for line in stdout.readlines():
        print line.strip().decode()

    session.close()