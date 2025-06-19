import smtplib
from dotenv import dotenv_values

settings = dotenv_values("C:\Users\Roman\PycharmProjects\centos_smtp\.env")

def connect_server(host):
    try:
        print "Setting connection to %s\n" % ''.join(host)
        smtp_server = smtplib.SMTP(host)
        print "Connection is set"
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

if __name__ == "__main__":
    my_host = str(settings.get('HOST'))
    source = str(settings.get('from_addr'))
    destination = str(settings.get('TO_ADDR'))
    msg = settings.get('message')
    print destination
    server = connect_server(my_host)
    send_message_smtp(source, destination, msg, server)

#print server.elho(hostname)
# try:
#     server.verify(to_addr)
#     server.sendmail(from_addr, to_addr, message)
#     print "Message is sent"
#     server.quit()
